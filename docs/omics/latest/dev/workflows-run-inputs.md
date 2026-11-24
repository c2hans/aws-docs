---
source_url: https://docs.aws.amazon.com/omics/latest/dev/workflows-run-inputs.html
---

# HealthOmics run inputs

If the workflow definition specifies input files for the workflow or workflow tasks, HealthOmics stages the files to a scratch volume that's dedicated to the workflow run. These input files are read-only, which prevents tasks from modifying potential inputs to other tasks in the workflow. For directory imports, the directories are also read-only.

Many genomics applications assume that index files are co-located with the sequence files (such as a companion `bai` file for a `bam` file). To include index files, specify them as task inputs in the workflow definition.

**Topics**
+ [Managing run parameters size](#run-input-file-options)
+ [Specify run parameters by reference](#run-parameters-uri)
+ [Amazon S3 input parameter formats](#s3-run-input-formats)
+ [Amazon S3 input archive states](#s3-run-input-archive)

## Managing run parameters size
<a name="run-input-file-options"></a>

When you start a run, you specify run inputs in the run parameters JSON object or file. You can specify up to 256 KB of run parameters for the workflow. You can use the following techniques to remain within this size constraint:
+ **Use directory imports**

  To specify a large number of input files, specify one parameter as the Amazon S3 location that contains all the files, rather than specifying a parameter for each file location. For more information, see the next topic (Amazon S3 input parameter formats).
+ **Specify the parameters by reference**

  To use more than 256 KB of run parameters, store the parameters in a JSON file in Amazon S3 and specify the file with the `parametersUri` field of **StartRun**. For more information, see [Specify run parameters by reference](#run-parameters-uri).
+ **Use a sample sheet**

  A sample sheet is a CSV or TSV file with one column for the fastq.gz address (or two for paired read) and additional columns for metadata such as sample names. You specify the sample sheet as a run input parameter instead of a parameter for each input file.

  Your workflow defines how your sample sheet maps to data structures in the workflow. While you could write code for sample sheets in WDL and CWL, they're more common in NextFlow. For an example, see [sample sheet](https://github.com/nf-core/scrnaseq/blob/master/assets/samplesheet.csv) on the **nf-core** GitHub site.

## Specify run parameters by reference
<a name="run-parameters-uri"></a>

Instead of passing run parameters inline in the **StartRun** request, you can store them in a JSON file in Amazon S3 and pass the Amazon S3 URI of the file in the `parametersUri` field. Use `parametersUri` when your run parameters are larger than the inline limit, for example when you list a large number of input files. You specify either `parameters` or `parametersUri` in a request, not both.

The following example starts a run with the parameters in a file in Amazon S3:

```
aws omics start-run \
     --workflow-id {{workflow-id}} \
     --role-arn arn:aws:iam::{{111122223333}}:role/{{OmicsRunRole}} \
     --output-uri s3://{{amzn-s3-demo-bucket}}/output \
     --parameters-uri s3://{{amzn-s3-demo-bucket}}/inputs/{{run-parameters.json}}
```

**Important**
For a run that uses `parametersUri`, HealthOmics validates the contents of the parameters file after **StartRun** returns. If the file isn't valid, **StartRun** still succeeds and the run fails with the failure reason `INVALID_RUN_PARAMETERS`. This behavior differs from inline parameters, where **StartRun** returns a validation error. For more information, see [How HealthOmics processes a parameters file](#run-parameters-uri-process).

### How HealthOmics processes a parameters file
<a name="run-parameters-uri-process"></a>

HealthOmics processes the parameters file in two steps.

1. **When you call **StartRun****

   HealthOmics checks the format of the URI and confirms that the object is in a bucket that your account owns. It reads the object's metadata with the service role that you specify for the run. It rejects the request if the object doesn't exist or if its size isn't within the allowed range. HealthOmics then reads one byte of the object with the credentials of the identity that calls **StartRun**, to confirm that the caller can read the file. HealthOmics records the entity tag (ETag) of the object. If any of these checks fail, **StartRun** returns an error and no run starts.

1. **After **StartRun** returns, before the run starts**

   HealthOmics reads the whole file with the service role, only if the object still has the ETag that it recorded. It validates the contents the same way that it validates inline parameters. The validation covers the JSON structure, the parameter names against the workflow's parameter template, the limits in the next section, and access to the Amazon S3 inputs. Where it can, HealthOmics also checks AWS KMS access to the input buckets. HealthOmics then stores a copy of the parameters. If the validation fails, the run fails with the failure reason `INVALID_RUN_PARAMETERS` before any compute starts, and the run's `statusMessage` describes the problem. For more information, see [Troubleshoot parameters file errors](#run-parameters-uri-errors).

Because HealthOmics reads the file twice, don't change or delete the file until the run is running. If the file changes before HealthOmics reads it the second time, the run fails. To use different parameters, upload a new file and start a new run.

### Requirements and limits for the parameters file
<a name="run-parameters-uri-requirements"></a>

The parameters file must meet the following requirements:
+ The file contains one JSON object. The object has the same parameter names and values as inline parameters.
+ The file size is from 3 bytes to 104,857,600 bytes (100 MiB).
+ The JSON object doesn't contain duplicate keys, doesn't have any content after the closing brace, and nests no more than 64 levels deep.
+ The object is in an Amazon S3 bucket that your account owns and that is in the same AWS Region as the run. HealthOmics doesn't accept a parameters file in a bucket that belongs to another account.
+ The object isn't in an archived storage state. For more information, see [Amazon S3 input archive states](#s3-run-input-archive).

The parameters in the file can reference up to 100 Amazon S3 buckets. For a run that uses `STATIC` or `DYNAMIC` run storage, they can reference up to 60,000 distinct Amazon S3 URIs. HealthOmics counts the URIs at any level of nesting in the file. For Nextflow, each URI in a comma-separated list of URIs counts. A URI that ends with a forward slash (a folder) or that uses a glob pattern counts as one URI, and a URI that appears more than once counts once. HealthOmics checks these limits before it checks access to any of the Amazon S3 objects. For a list of all quotas, see [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows).

### Permissions for the parameters file
<a name="run-parameters-uri-permissions"></a>

Both the service role for the run and the identity that calls **StartRun** must be able to read the parameters file. This requirement is in addition to the permissions that you need for inline parameters. The following table lists the permissions.

| Identity | Permission | Purpose |
| --- | --- | --- |
| Service role for the run | s3:GetObject on the parameters file | HealthOmics reads the file's metadata and contents with this role. |
| Service role for the run | kms:Decrypt on the AWS KMS key of the parameters file, if the file uses SSE-KMS encryption | HealthOmics decrypts the file when it reads it. |
| Service role for the run | kms:Encrypt and kms:Decrypt on the AWS KMS key of each input bucket whose default encryption is SSE-KMS | HealthOmics checks KMS access to your input buckets where it can. If your role doesn't have KMS access to a key, the run might fail after it starts, instead of failing during validation. |
| Service role for the run | s3:ListBucket on the bucket of the parameters file (optional) | When the file is missing, Amazon S3 returns a clearer error to HealthOmics if the role has this permission. |
| Identity that calls StartRun | s3:GetObject on the parameters file, and kms:Decrypt on its AWS KMS key if the file is encrypted | HealthOmics reads one byte of the file as the caller to confirm that the caller can read it. |
| Identity that calls StartRun | kms:Decrypt on the default AWS KMS key of each input bucket that uses SSE-KMS | HealthOmics checks this access where it can, as it does for inline parameters. For a run that uses parametersUri, a failed check fails the run with INVALID\_RUN\_PARAMETERS instead of returning an error from StartRun. |

The following example policy statements for the service role allow HealthOmics to read a parameters file that is encrypted with a customer managed key:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/inputs/{{run-parameters.json}}"
    },
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:{{us-west-2}}:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
    }
  ]
}
```

The following requirements also apply:
+ **Same account** – Your account must own the bucket of the parameters file, and the service role must be in your account. HealthOmics rejects a parameters file in a bucket that another account owns.
+ **Same Region** – The bucket must be in the same Region as the run. HealthOmics rejects a parameters file in a bucket in another Region.
+ **Session policies** – If you start the run with a session policy, check that the session policy also allows read access to the parameters file.
+ **Unchanged requirements** – The trust policy of the service role, the `iam:PassRole` permission, and the KMS requirements for your input buckets are the same as for runs that use inline parameters. For more information, see [Service roles for AWS HealthOmics](permissions-service.md).

### How HealthOmics stores and deletes your parameters
<a name="run-parameters-uri-storage"></a>

HealthOmics never modifies your parameters file and doesn't copy it to another location that you own. After it validates the parameters, HealthOmics stores the following copies for the run in storage that HealthOmics owns:
+ A verbatim copy of your parameters file.
+ A copy of the parameters that is prepared for the workflow engine.
+ A list of the Amazon S3 buckets that the parameters reference.

HealthOmics encrypts these copies at rest. If a run fails validation after HealthOmics has read your file, HealthOmics might keep a copy of the file that it read, so that you can inspect it with **GetRun**. When you delete a run, HealthOmics attempts to delete these copies. Your parameters file stays in your bucket, and deleting your parameters file doesn't delete the copies.

### Get the parameters of a run
<a name="run-parameters-uri-getrun"></a>

For a run that you start with `parametersUri`, **GetRun** returns the `parametersUri` field instead of the inline `parameters` field. The field contains one of the following values:
+ A presigned HTTPS URL for the copy of your parameters file that HealthOmics stores for the run. The URL expires after at most 10 minutes. To get a new URL, call **GetRun** again. The URL gives access to the copy of that one run only.
+ The `s3://` URI that you submitted. HealthOmics returns this value, as plain text and not as a presigned URL, until it has stored a copy of the file. It can also return this value for a run that failed validation, if HealthOmics has no copy of the file that it read. For the reason that a run failed, check `failureReason` and `statusMessage`.

**Important**
Treat the presigned URL as a credential. Anyone who has the URL can read the parameters until the URL expires. Don't write the URL to logs, tickets, or chat messages, and don't share it.

Permission to call **GetRun** is enough to get the presigned URL and read the stored copy. It doesn't require `s3:GetObject` permission on your parameters file or `kms:Decrypt` permission on its key.

For a run that uses `parametersUri`, the `resourceDigests` field of the **GetRun** response doesn't contain an entry for each input file.

### Security best practices for parameters files
<a name="run-parameters-uri-practices"></a>
+ Limit the permissions of the service role to the folder that contains the parameters file and the input data, instead of the whole bucket.
+ Keep the parameters file in a bucket of your own account, in the Region of the run. To keep earlier versions of the file, turn on versioning for the bucket. HealthOmics also stores a copy of the parameters of a validated run, which you can get with **GetRun**.
+ Parameters can contain sample or patient identifiers. Anyone who has permission to call **GetRun** for a run can read its parameters, whether you specify them inline or by reference. Restrict who can call **GetRun** and who can read the bucket that contains your parameters files.
+ If the parameters are sensitive, encrypt the file with SSE-KMS, and make sure that both the service role and the identity that calls **StartRun** can decrypt it. SSE-KMS controls access to your file only. Access to the copy that HealthOmics stores is controlled by permission to call **GetRun**.
+ Don't put secrets or credentials in the parameters file.
+ Don't write the presigned URL that **GetRun** returns to logs, tickets, or chat messages.

### Limitations of parameters files
<a name="run-parameters-uri-limitations"></a>
+ **Reruns** – You can't use the `runId` field of **StartRun** to rerun a run that you started with `parametersUri`, and a rerun request can't include `parametersUri`. To repeat such a run, call **StartRun** with the workflow and a `parametersUri`.
+ **Batch runs** – **StartRunBatch** doesn't support `parametersUri`. If you include `parametersUri` in `defaultRunSetting`, in an `inlineSettings` entry, or in an `s3UriSettings` file, HealthOmics ignores it, as it does any unrecognized field. The runs start without those parameters, and a run that needs them fails. To use a parameters file, start each run with **StartRun**.

### Troubleshoot parameters file errors
<a name="run-parameters-uri-errors"></a>

The following tables list common messages for runs that use `parametersUri`. The exact wording of a message can change, and a message can include additional text, such as the Amazon S3 URI of your parameters file.

**Errors that **StartRun** returns**

| Message | Cause and action |
| --- | --- |
| Specify either parameters or parametersUri, not both. | The request includes both fields. Remove one of them. |
| parametersUri must be a valid s3:// object URI | The value isn't an Amazon S3 URI of an object. Specify a URI in the format s3://{{bucket}}/{{key}}. |
| parametersUri object not found | The object doesn't exist. Check the bucket and the key. |
| parametersUri object could not be read (check that it exists, that your account owns the bucket, and that the run role can read it) | HealthOmics can't read the object with the service role. Check that the object exists, that your account owns the bucket, and that the service role has s3:GetObject on the object. To get a more specific message, you can optionally grant s3:ListBucket to the service role. |
| parametersUri object is empty | The object is smaller than 3 bytes. |
| parametersUri object size ({{n}} bytes) exceeds the maximum of 104857600 bytes | The object is larger than 104,857,600 bytes (100 MiB). Reduce the size of the file. |
| parametersUri must reference a bucket you own | The URI refers to a bucket that HealthOmics owns. Use a bucket in your account. |
| parametersUri object changed while StartRun was checking it | The file changed while StartRun was reading it. Wait until the upload finishes, and call StartRun again. |
| Transient S3 error reading parametersUri; retry the request | Amazon S3 returned a temporary error. Call StartRun again. |
| No caller permission to read | The identity that calls StartRun doesn't have s3:GetObject on the parameters file. Add the permission. |
| No caller permission to decrypt | The identity that calls StartRun doesn't have kms:Decrypt on the AWS KMS key of the parameters file. Add the permission. |

**Failure messages for a run with the failure reason `INVALID_RUN_PARAMETERS`**

Find these messages in the `statusMessage` field of the run.

| Message | Cause and action |
| --- | --- |
| The parametersUri object {{uri}} changed after the run was submitted. Start a new run. | The file changed after you called StartRun. Upload the file again, and start a new run. |
| The parametersUri object {{uri}} could not be read. The run's account must own the bucket, and the run role needs s3:GetObject on the object (and kms:Decrypt for a KMS-encrypted object). | Check bucket ownership, and add the missing permissions to the service role. |
| The parametersUri object was not found | The file was deleted after you called StartRun. Upload the file again, and start a new run. |
| The parametersUri bucket is not in this run's Region | Use a bucket in the same Region as the run. |
| The parametersUri object is archived | Restore the object, or copy it to a storage class that HealthOmics can read in real time. |
| The parametersUri object is not a valid JSON object | The file isn't one JSON object, has duplicate keys, or has content after the object. The message includes the line and column of the problem when they are available. |
| The parametersUri object nests deeper than 64 levels | Reduce the nesting of the JSON object. |
| The run parameters reference {{n}} S3 objects | The parameters reference more distinct Amazon S3 URIs than the quota allows, which is 60,000 for a run with STATIC or DYNAMIC run storage. Use folder URIs in place of a list of files. |
| The run parameters reference {{n}} S3 buckets | The parameters reference more than 100 Amazon S3 buckets. |

## Amazon S3 input parameter formats
<a name="s3-run-input-formats"></a>

For an input parameter that accepts an Amazon S3 location, the parameter can specify the location of one file or a whole directory of files. Using a directory has the following advantages:
+ Convenience – You specify the directory name as the parameter. You don't list each file name.
+ Compactness – The input parameter maximum file size is 256 KB. If you provide a long list of input file names, you can exceed this maximum.

Amazon S3 is a flat object-storage system, so it doesn't support directories. You group files into a "directory" by giving each file the same object key prefix. For more information about Amazon S3 object key prefixes, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).

 HealthOmics interprets the input parameter value as follows:
+ If the Amazon S3 location doesn't end with a forward slash or use the glob pattern, HealthOmics expects the parameter value to be the key for one Amazon S3 object.

  For example, you specify `s3://myfiles/runs/inputs/a/file1.fastq` to input file1.fastq
+ If the Amazon S3 location ends with a forward slash, HealthOmics interprets the parameter value as an Amazon S3 prefix. It loads all the Amazon S3 objects with that prefix.

  For example, you can specify `s3://myfiles/runs/inputs/a/` to load all objects whose keys start with this prefix.
+ For Nextflow, HealthOmics paritally supports the glob pattern for Amazon S3 URIs in input parameters.

  For example, you can specify `“s3://myfiles/runs/inputs/a/*.gz”` to input all .gz files whose keys start with this prefix.

### Nextflow Handling of Glob pattern in Amazon S3 inputs
<a name="wd-nextflow-s3-formats"></a>

| Glob Pattern | HealthOmics Match Behavior | Notes |
| --- | --- | --- |
| s3://bucket/directory/\*.txt | Matches all .txt objects at any depth under the prefix s3://bucket/directory/. For example, matches s3://bucket/directory/abc.txt or s3://bucket/directory/subDir/123.txt etc. |  |
| s3://bucket/directory/\*\*/\*.txt | Matches all .txt objects at any depth under the prefix s3://bucket/directory/. For example, matches s3://bucket/directory/abc.txt or s3://bucket/directory/subDir/123.txt etc. | In S3, \*\* is equivalent to \*. |
| s3://bucket/directory/{a,b}.txt | s3://bucket/directory/a.txt, s3://bucket/directory/b.txt |  |
| s3://bucket/directory/?.txt | Matches objects at the prefix root whose filename is a single character followed by .txt. For example, it matches s3://bucket/directory/a.txt but not s3://bucket/directory/someDir/a.txt or s3://bucket/directory/someDir/subDir/a.txt |  |
| s3://bucket/directory/[0-9].txt | s3://bucket/directory/0.txt, s3://bucket/directory/1.txt, ... ,s3://bucket/directory/9.txt |  |
| s3://bucket/directory/[0-9].txt | s3://bucket/directory/1.txt, s3://bucket/directory/2.txt, s3://bucket/directory/3.txt |  |
| s3://bucket/directory/[0-9].txt | s3://bucket/directory/b.txt, s3://bucket/directory/c.txt, ... ,s3://bucket/directory/Y.txt |  |

### Language-specific handling of double-slash in Amazon S3 inputs
<a name="wd-s3-formats"></a>

HealthOmics retains the native engine behavior for each workflow engine when handling double-slashes in Amazon S3 URIs, so that you don't need to make any changes to your workflows when you migrate them to HealthOmics. The following sections describe how each engine handles various scenarios.

#### WDL
<a name="wd-wdl-s3-formats"></a>

If the input parameter includes a double-slash in the middle or at the end of the URI, the WDL engine retains the double-slash.

| Input parameter | Expected location |
| --- | --- |
| s3://myfiles/runs/inputs//file1.fastq | s3://myfiles/runs/inputs//file1.fastq |
| s3://myfiles/runs/inputs// | s3://myfiles/runs/inputs// |

#### Nextflow
<a name="wd-nextflow-s3-doubleslash"></a>

If the input parameter includes a double-slash in the middle of the URI, the Nextflow engine retains double-slash. For a double-slash at the end of the URI, the Nextflow engine resolves it to a single slash.

| Input parameter | Expected location |
| --- | --- |
| s3://myfiles/runs/inputs//file1.fastq | s3://myfiles/runs/inputs//file1.fastq |
| s3://myfiles//runs/inputs//\*.gz | s3://myfiles//runs/inputs//\*.gz |
| s3://myfiles//runs/inputs// | s3://myfiles//runs/inputs/ |

#### CWL
<a name="wd-cwl-s3-formats"></a>

If the input parameter includes a double-slash in the middle or at the end of the URI, the CWL engine retains the double-slash.

| Input parameter | Expected location |
| --- | --- |
| s3://myfiles//runs/inputs//file1.fastq | s3://myfiles//runs/inputs//file1.fastq |
| s3://myfiles//runs/inputs// | s3://myfiles//runs/inputs// |

## Amazon S3 input archive states
<a name="s3-run-input-archive"></a>

HealthOmics can retrieve Amazon S3 objects that S3 delivers in real time. For objects that are in the following archived storage states, **restore** the objects to make them available to HealthOmics:
+ Flexible Retrieval or Deep Archive storage classes in Amazon S3 Glacier.
+ Archived Access or Deep Archive Access tiers in Intelligent tiering.

For information about restoring objects, see [ Restoring an archived object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/restoring-objects.html) in the *Amazon S3 User Guide*.
