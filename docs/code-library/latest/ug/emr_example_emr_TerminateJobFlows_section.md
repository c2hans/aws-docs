---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/emr_example_emr_TerminateJobFlows_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `TerminateJobFlows` with an AWS SDK
<a name="emr_example_emr_TerminateJobFlows_section"></a>

The following code examples show how to use `TerminateJobFlows`.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/emr#code-examples).

```
def terminate_cluster(cluster_id, emr_client):
    """
    Terminates a cluster. This terminates all instances in the cluster and cannot
    be undone. Any data not saved elsewhere, such as in an Amazon S3 bucket, is lost.

    :param cluster_id: The ID of the cluster to terminate.
    :param emr_client: The Boto3 EMR client object.
    """
    try:
        emr_client.terminate_job_flows(JobFlowIds=[cluster_id])
        logger.info("Terminated cluster %s.", cluster_id)
    except ClientError:
        logger.exception("Couldn't terminate cluster %s.", cluster_id)
        raise
```
+  For API details, see [TerminateJobFlows](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/TerminateJobFlows) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        DATA lt_cluster_ids TYPE /aws1/cl_emrxmlstringlist_w=>tt_xmlstringlist.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( iv_cluster_id ) TO lt_cluster_ids.

        lo_emr->terminatejobflows(
          it_jobflowids = lt_cluster_ids
        ).
        MESSAGE 'EMR cluster terminated successfully.' TYPE 'I'.
      CATCH /aws1/cx_emrinternalservererr INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [TerminateJobFlows](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------
