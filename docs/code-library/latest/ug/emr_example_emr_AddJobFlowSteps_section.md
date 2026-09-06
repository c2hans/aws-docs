---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/emr_example_emr_AddJobFlowSteps_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AddJobFlowSteps` with an AWS SDK
<a name="emr_example_emr_AddJobFlowSteps_section"></a>

The following code examples show how to use `AddJobFlowSteps`.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/emr#code-examples).
Add a Spark step, which is run by the cluster as soon as it is added.

```
def add_step(cluster_id, name, script_uri, script_args, emr_client):
    """
    Adds a job step to the specified cluster. This example adds a Spark
    step, which is run by the cluster as soon as it is added.

    :param cluster_id: The ID of the cluster.
    :param name: The name of the step.
    :param script_uri: The URI where the Python script is stored.
    :param script_args: Arguments to pass to the Python script.
    :param emr_client: The Boto3 EMR client object.
    :return: The ID of the newly added step.
    """
    try:
        response = emr_client.add_job_flow_steps(
            JobFlowId=cluster_id,
            Steps=[
                {
                    "Name": name,
                    "ActionOnFailure": "CONTINUE",
                    "HadoopJarStep": {
                        "Jar": "command-runner.jar",
                        "Args": [
                            "spark-submit",
                            "--deploy-mode",
                            "cluster",
                            script_uri,
                            *script_args,
                        ],
                    },
                }
            ],
        )
        step_id = response["StepIds"][0]
        logger.info("Started step with ID %s", step_id)
    except ClientError:
        logger.exception("Couldn't start step %s with URI %s.", name, script_uri)
        raise
    else:
        return step_id
```
Run an Amazon EMR File System (EMRFS) command as a job step on a cluster. This can be used to automate EMRFS commands on a cluster instead of running commands manually through an SSH connection.

```
import boto3
from botocore.exceptions import ClientError

def add_emrfs_step(command, bucket_url, cluster_id, emr_client):
    """
    Add an EMRFS command as a job flow step to an existing cluster.

    :param command: The EMRFS command to run.
    :param bucket_url: The URL of a bucket that contains tracking metadata.
    :param cluster_id: The ID of the cluster to update.
    :param emr_client: The Boto3 Amazon EMR client object.
    :return: The ID of the added job flow step. Status can be tracked by calling
             the emr_client.describe_step() function.
    """
    job_flow_step = {
        "Name": "Example EMRFS Command Step",
        "ActionOnFailure": "CONTINUE",
        "HadoopJarStep": {
            "Jar": "command-runner.jar",
            "Args": ["/usr/bin/emrfs", command, bucket_url],
        },
    }

    try:
        response = emr_client.add_job_flow_steps(
            JobFlowId=cluster_id, Steps=[job_flow_step]
        )
        step_id = response["StepIds"][0]
        print(f"Added step {step_id} to cluster {cluster_id}.")
    except ClientError:
        print(f"Couldn't add a step to cluster {cluster_id}.")
        raise
    else:
        return step_id

def usage_demo():
    emr_client = boto3.client("emr")
    # Assumes the first waiting cluster has EMRFS enabled and has created metadata
    # with the default name of 'EmrFSMetadata'.
    cluster = emr_client.list_clusters(ClusterStates=["WAITING"])["Clusters"][0]
    add_emrfs_step(
        "sync", "s3://elasticmapreduce/samples/cloudfront", cluster["Id"], emr_client
    )

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [AddJobFlowSteps](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/AddJobFlowSteps) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        " Build args list for Spark submit
        DATA lt_args TYPE /aws1/cl_emrxmlstringlist_w=>tt_xmlstringlist.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( 'spark-submit' ) TO lt_args.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( '--deploy-mode' ) TO lt_args.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( 'cluster' ) TO lt_args.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( iv_script_uri ) TO lt_args.
        APPEND LINES OF it_script_args TO lt_args.

        " Create step configuration
        DATA(lo_hadoop_jar_step) = NEW /aws1/cl_emrhadoopjarstepcfg(
          iv_jar = 'command-runner.jar'
          it_args = lt_args
        ).

        DATA(lo_step_config) = NEW /aws1/cl_emrstepconfig(
          iv_name = iv_name
          iv_actiononfailure = 'CONTINUE'
          io_hadoopjarstep = lo_hadoop_jar_step
        ).

        DATA lt_steps TYPE /aws1/cl_emrstepconfig=>tt_stepconfiglist.
        APPEND lo_step_config TO lt_steps.

        DATA(lo_result) = lo_emr->addjobflowsteps(
          iv_jobflowid = iv_cluster_id
          it_steps = lt_steps
        ).

        " Get first step ID
        DATA(lt_step_ids) = lo_result->get_stepids( ).
        READ TABLE lt_step_ids INDEX 1 INTO DATA(lo_step_id_obj).
        IF sy-subrc = 0.
          ov_step_id = lo_step_id_obj->get_value( ).
          MESSAGE |Step added with ID { ov_step_id }| TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_emrinternalservererr INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [AddJobFlowSteps](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------
