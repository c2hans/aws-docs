---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets.html
---

# Use SageMaker Processing for distributed feature engineering of terabyte-scale ML datasets
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets"></a>

*Chris Boomhower, Amazon Web Services*

## Summary
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets-summary"></a>

Many terabyte-scale or larger datasets often consist of a hierarchical folder structure, and the files in the dataset sometimes share interdependencies. For this reason, machine learning (ML) engineers and data scientists must make thoughtful design decisions to prepare such data for model training and inference. This pattern demonstrates how you can use manual macrosharding and microsharding techniques in combination with Amazon SageMaker Processing and virtual CPU (vCPU) parallelization to efficiently scale feature engineering processes for complicated big data ML datasets.

This pattern defines *macrosharding* as the splitting of data directories across multiple machines for processing, and *microsharding* as the splitting of data on each machine across multiple processing threads. The pattern demonstrates these techniques by using Amazon SageMaker with sample time-series waveform records from the [PhysioNet MIMIC-III](https://physionet.org/content/mimic3wdb/1.0/) dataset. By implementing the techniques in this pattern, you can minimize the processing time and costs for feature engineering while maximizing resource utilization and throughput efficiency. These optimizations rely on distributed SageMaker Processing on Amazon Elastic Compute Cloud (Amazon EC2) instances and vCPUs for similar, large datasets, regardless of data type.

## Prerequisites and limitations
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets-prereqs"></a>

**Prerequisites**
+ Access to SageMaker notebook instances or SageMaker Studio, if you want to implement this pattern for your own dataset. If you are using Amazon SageMaker for the first time, see [Get started with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html) in the AWS documentation.
+ SageMaker Studio, if you want to implement this pattern with the [PhysioNet MIMIC-III](https://physionet.org/content/mimic3wdb/1.0/) sample data.
+ The pattern uses SageMaker Processing, but doesn’t require any experience running SageMaker Processing jobs.

**Limitations**
+ This pattern is well suited to ML datasets that include interdependent files. These interdependencies benefit the most from manual macrosharding and running multiple, single-instance SageMaker Processing jobs in parallel. For datasets where such interdependencies do not exist, the `ShardedByS3Key` feature in SageMaker Processing might be a better alternative to macrosharding, because it sends sharded data to multiple instances that are managed by the same Processing job. However, you can implement this pattern’s microsharding strategy in both scenarios to best utilize instance vCPUs.

**Product versions**
+ Amazon SageMaker Python SDK version 2

## Architecture
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets-architecture"></a>

**Target technology stack**
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon SageMaker

**Target architecture**

*Macrosharding and distributed EC2 instances*

The 10 parallel processes represented in this architecture reflect the structure of the MIMIC-III dataset. (Processes are represented by ellipses for diagram simplification.) A similar architecture applies to any dataset when you use manual macrosharding. In the case of MIMIC-III, you can use the dataset's raw structure to your advantage by processing each patient group folder separately, with minimal effort. In the following diagram, the record groups block appears on the left (1). Given the distributed nature of the data, it makes sense to shard by patient group.

![Architecture for microsharding and distributed EC2 instances](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e7a90b31-de8f-41fd-bb3f-c7c6100fc306/images/c19a8f87-ac59-458e-89cb-50be17ca4a0c.png)

However, manually sharding by patient group means that a separate Processing job is required for each patient group folder, as you can see in the middle section of the diagram (2), instead of a single Processing job with multiple EC2 instances. Because MIMIC-III's data includes both binary waveform files and matching text-based header files, and there is a required dependency on the [wfdb library](https://wfdb.readthedocs.io/en/latest/) for binary data extraction, all the records for a specific patient must be made available on the same instance. The only way to be certain that each binary waveform file's associated header file is also present is to implement manual sharding to run each shard within its own Processing job, and to specify `s3_data_distribution_type='FullyReplicated'` when you define the Processing job input. Alternatively, if all data were available in a single directory and no dependencies existed between files, a more suitable option might be to launch a single Processing job with multiple EC2 instances and `s3_data_distribution_type='ShardedByS3Key'` specified. Specifying `ShardedByS3Key `as the Amazon S3 data distribution type directs SageMaker to manage data sharding automatically across instances.

Launching a Processing job for each folder is a cost-efficient way to preprocess the data, because running multiple instances concurrently saves time. For additional cost and time savings, you can use microsharding within each Processing job.

*Microsharding and parallel vCPUs*

Within each Processing job, the grouped data is further divided to maximize use of all available vCPUs on the SageMaker fully managed EC2 instance. The blocks in the middle section of the diagram (2) depict what happens within each primary Processing job. The contents of the patient record folders are flattened and divided evenly based on the  number of available vCPUs on the instance. After the folder contents are divided, the evenly sized set of files are distributed across all vCPUs for processing. When processing is complete, the results from each vCPU are combined into a single data file for each Processing job.

In the attached code, these concepts are represented in the following section of the `src/feature-engineering-pass1/preprocessing.py` file.

```
def chunks(lst, n):
    """
    Yield successive n-sized chunks from lst.

    :param lst: list of elements to be divided
    :param n: number of elements per chunk
    :type lst: list
    :type n: int
    :return: generator comprising evenly sized chunks
    :rtype: class 'generator'
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Generate list of data files on machine
data_dir = input_dir
d_subs = next(os.walk(os.path.join(data_dir, '.')))[1]
file_list = []
for ds in d_subs:
    file_list.extend(os.listdir(os.path.join(data_dir, ds, '.')))
dat_list = [os.path.join(re.split('_|\.', f)[0].replace('n', ''), f[:-4]) for f in file_list if f[-4:] == '.dat']

# Split list of files into sub-lists
cpu_count = multiprocessing.cpu_count()
splits = int(len(dat_list) / cpu_count)
if splits == 0: splits = 1
dat_chunks = list(chunks(dat_list, splits))

# Parallelize processing of sub-lists across CPUs
ws_df_list = Parallel(n_jobs=-1, verbose=0)(delayed(run_process)(dc) for dc in dat_chunks)

# Compile and pickle patient group dataframe
ws_df_group = pd.concat(ws_df_list)
ws_df_group = ws_df_group.reset_index().rename(columns={'index': 'signal'})
ws_df_group.to_json(os.path.join(output_dir, group_data_out))
```

A function, `chunks`, is first defined to consume a given list by dividing it into evenly sized chunks of length `n `and by returning these results as a generator. Next, the data is flattened across patient folders by compiling a list of all binary waveform files that are present. After this is done, the number of vCPUs available on the EC2 instance is obtained. The list of binary waveform files is evenly divided across these vCPUs by calling `chunks`, and then each waveform sublist is processed on its own vCPU by using [joblib's Parallel class](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html). Results are automatically combined into a single list of dataframes by the Processing job, which SageMaker then processes further before writing it to Amazon S3 upon job completion. In this example, there are 10 files written to Amazon S3 by the Processing jobs (one for each job).

When all the initial Processing jobs are complete, a secondary Processing job, which is shown in the block to the right of the diagram (3) combines the output files produced by each primary Processing job and writes the combined output to Amazon S3 (4).

## Tools
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets-tools"></a>

**Tools**
+ [Python](https://www.python.org/) – The sample code used for this pattern is Python (version 3).
+ [SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) – Amazon SageMaker Studio is a web-based, integrated development environment (IDE) for machine learning that lets you build, train, debug, deploy, and monitor your machine learning models. You run SageMaker Processing jobs by using Jupyter notebooks inside SageMaker Studio.
+ [SageMaker Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) – Amazon SageMaker Processing provides a simplified way to run your data processing workloads. In this pattern, the feature engineering code is implemented at scale by using SageMaker Processing jobs.

**Code**

The attached .zip file provides the complete code for this pattern. The following section describes the steps to build the architecture for this pattern. Each step is illustrated by sample code from the attachment.

## Epics
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets-epics"></a>

### Set up your SageMaker Studio environment
<a name="set-up-your-sagemaker-studio-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access Amazon SageMaker Studio. | Onboard to SageMaker Studio in your AWS account by following the directions provided in the [Amazon SageMaker documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html). | Data scientist, ML engineer |
| Install the wget utility. | Install *wget* if you onboarded with a new SageMaker Studio configuration or if you've never used these utilities in SageMaker Studio before. <br />To install, open a terminal window in the SageMaker Studio console and run the following command:<pre>sudo yum install wget</pre> | Data scientist, ML engineer |
| Download and unzip the sample code. | Download the `attachments.zip` file in the *Attachments* section. In a terminal window, navigate to the folder where you downloaded the file and extract its contents:<pre>unzip attachment.zip</pre><br />Navigate to the folder where you extracted the .zip file, and extract the contents of the `Scaled-Processing.zip` file.<pre>unzip Scaled-Processing.zip</pre> | Data scientist, ML engineer |
| Download the sample dataset from physionet.org and upload it to Amazon S3. | Run the `get_data.ipynb` Jupyter notebook within the folder that contains the `Scaled-Processing` files. This notebook downloads a sample MIMIC-III dataset from [physionet.org](https://physionet.org) and uploads it to your SageMaker Studio session bucket in Amazon S3. | Data scientist, ML engineer |

### Configure the first preprocessing script
<a name="configure-the-first-preprocessing-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Flatten the file hierarchy across all subdirectories. | In large datasets such as MIMIC-III, files are often distributed across multiple subdirectories even within a logical parent group. Your script should be configured to flatten all group files across all subdirectories, as the following code demonstrates.<pre># Generate list of .dat files on machine<br />data_dir = input_dir<br />d_subs = next(os.walk(os.path.join(data_dir, '.')))[1]<br />file_list = []<br />for ds in d_subs:<br />    file_list.extend(os.listdir(os.path.join(data_dir, ds, '.')))<br />dat_list = [os.path.join(re.split('_|\.', f)[0].replace('n', ''), f[:-4]) for f in file_list if f[-4:] == '.dat']</pre>    The example code snippets in this epic are from the `src/feature-engineering-pass1/preprocessing.py` file, which is provided in the attachment. | Data scientist, ML engineer |
| Divide files into subgroups based on vCPU count. | Files should be divided into evenly sized subgroups, or chunks, depending on the number of vCPUs present on the instance that runs the script. For this step, you can implement code similar to the following.<pre># Split list of files into sub-lists<br />cpu_count = multiprocessing.cpu_count()<br />splits = int(len(dat_list) / cpu_count)<br />if splits == 0: splits = 1<br />dat_chunks = list(chunks(dat_list, splits))</pre> | Data scientist, ML engineer |
| Parallelize processing of subgroups across vCPUs. | Script logic should be configured to process all subgroups in parallel. To do this, use the Joblib library's `Parallel `class and `delayed `method as follows. <pre># Parallelize processing of sub-lists across CPUs<br />ws_df_list = Parallel(n_jobs=-1, verbose=0)(delayed(run_process)(dc) for dc in dat_chunks)</pre> | Data scientist, ML engineer |
| Save single file group output to Amazon S3. | When parallel vCPU processing is complete, the results from each vCPU should be combined and uploaded to the file group's S3 bucket path. For this step, you can use code similar to the following.<pre># Compile and pickle patient group dataframe<br />ws_df_group = pd.concat(ws_df_list)<br />ws_df_group = ws_df_group.reset_index().rename(columns={'index': 'signal'})<br />ws_df_group.to_json(os.path.join(output_dir, group_data_out))</pre> | Data scientist, ML engineer |

### Configure the second preprocessing script
<a name="configure-the-second-preprocessing-script"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Combine data files produced across all Processing jobs that ran the first script. | The previous script outputs a single file for each SageMaker Processing job that processes a group of files from the dataset.  Next, you need to combine these output files into a single object and write a single output dataset to Amazon S3. This is demonstrated in the `src/feature-engineering-pass1p5/preprocessing.py` file, which is provided in the attachment, as follows.<pre>def write_parquet(wavs_df, path):<br />    """<br />    Write waveform summary dataframe to S3 in parquet format.<br />    <br />    :param wavs_df: waveform summary dataframe<br />    :param path: S3 directory prefix<br />    :type wavs_df: pandas dataframe<br />    :type path: str<br />    :return: None<br />    """<br />    extra_args = {"ServerSideEncryption": "aws:kms"}<br />    wr.s3.to_parquet(<br />        df=wavs_df,<br />        path=path,<br />        compression='snappy',<br />        s3_additional_kwargs=extra_args)<br /> <br /> <br />def combine_data():<br />    """<br />    Get combined data and write to parquet.<br />    <br />    :return: waveform summary dataframe<br />    :rtype: pandas dataframe<br />    """<br />    wavs_df = get_data()<br />    wavs_df = normalize_signal_names(wavs_df)<br />    write_parquet(wavs_df, "s3://{}/{}/{}".format(bucket_xform, dataset_prefix, pass1p5out_data))<br /> <br />    return wavs_df<br /> <br /> <br />wavs_df = combine_data()</pre> | Data scientist, ML engineer |

### Run Processing jobs
<a name="run-processing-jobs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the first Processing job. | To perform macrosharding, run a separate Processing job for each file group. Microsharding is performed inside each Processing job, because each job runs your first script. The following code demonstrates how to launch a Processing job for each file group directory in the following snippet (included in `notebooks/FeatExtract_Pass1.ipynb`).<pre>pat_groups = list(range(30,40))<br />ts = str(int(time.time()))<br /> <br />for group in pat_groups:<br />    sklearn_processor = SKLearnProcessor(framework_version='0.20.0',<br />                                     role=role,<br />                                     instance_type='ml.m5.4xlarge',<br />                                     instance_count=1,<br />                                     volume_size_in_gb=5)<br />    sklearn_processor.run(<br />        code='../src/feature-engineering-pass1/preprocessing.py',<br />        job_name='-'.join(['scaled-processing-p1', str(group), ts]),<br />        arguments=[<br />            "input_path", "/opt/ml/processing/input",<br />            "output_path", "/opt/ml/processing/output",<br />            "group_data_out", "ws_df_group.json"<br />        ],<br />        inputs=<br />        [<br />            ProcessingInput(<br />                source=f's3://{sess.default_bucket()}/data_inputs/{group}',<br />                destination='/opt/ml/processing/input',<br />                s3_data_distribution_type='FullyReplicated'<br />            )<br />        ],<br />        outputs=<br />        [<br />            ProcessingOutput(<br />                source='/opt/ml/processing/output',<br />                destination=f's3://{sess.default_bucket()}/data_outputs/{group}'<br />            )<br />        ],<br />        wait=False<br />    )</pre> | Data scientist, ML engineer |
| Run the second Processing job. | To combine the outputs generated by the first set of processing jobs and perform any additional computations for preprocessing, you run your second script by using a single SageMaker Processing job. The following code demonstrates this (included in `notebooks/FeatExtract_Pass1p5.ipynb`).<pre>ts = str(int(time.time()))<br />bucket = sess.default_bucket()<br />     <br />sklearn_processor = SKLearnProcessor(framework_version='0.20.0',<br />                                 role=role,<br />                                 instance_type='ml.t3.2xlarge',<br />                                 instance_count=1,<br />                                 volume_size_in_gb=5)<br />sklearn_processor.run(<br />    code='../src/feature-engineering-pass1p5/preprocessing.py',<br />    job_name='-'.join(['scaled-processing', 'p1p5', ts]),<br />    arguments=['bucket', bucket,<br />               'pass1out_prefix', 'data_outputs',<br />               'pass1out_data', 'ws_df_group.json',<br />               'pass1p5out_data', 'waveform_summary.parquet',<br />               'statsdata_name', 'signal_stats.csv'],<br />    wait=True<br />)</pre> | Data scientist, ML engineer |

## Related resources
<a name="use-sagemaker-processing-for-distributed-feature-engineering-of-terabyte-scale-ml-datasets-resources"></a>
+ [Onboard to Amazon SageMaker Studio Using Quick Start](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html) (SageMaker documentation)
+ [Process Data](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) (SageMaker documentation)
+ [Data Processing with scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/use-scikit-learn-processing-container.html) (SageMaker documentation)
+ [joblib.Parallel documentation](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html)
+ Moody, B., Moody, G., Villarroel, M., Clifford, G. D., & Silva, I. (2020). [MIMIC-III Waveform Database](https://doi.org/10.13026/c2607m) (version 1.0). *PhysioNet*.
+ Johnson, A. E. W., Pollard, T. J., Shen, L., Lehman, L. H., Feng, M., Ghassemi, M., Moody, B., Szolovits, P., Celi, L. A., & Mark, R. G. (2016). [MIMIC-III, a freely accessible critical care database](https://dx.doi.org/10.1038/sdata.2016.35). Scientific Data, 3, 160035.
+ [MIMIC-III Waveform Database license](https://physionet.org/content/mimic3wdb/1.0/LICENSE.txt)

## Attachments
<a name="attachments-e7a90b31-de8f-41fd-bb3f-c7c6100fc306"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/e7a90b31-de8f-41fd-bb3f-c7c6100fc306/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
