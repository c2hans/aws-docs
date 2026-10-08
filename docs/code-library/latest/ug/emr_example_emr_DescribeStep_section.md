---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/emr_example_emr_DescribeStep_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeStep` with an AWS SDK or CLI
<a name="emr_example_emr_DescribeStep_section"></a>

The following code examples show how to use `DescribeStep`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Getting started with big data processing clusters](emr_example_emr_GettingStarted_037_section.md)

------
#### [ CLI ]

**AWS CLI**
The following command describes a step with the step ID `s-3LZC0QUT43AM` in a cluster with the cluster ID `j-3SD91U2E1L2QX`:

```
aws emr describe-step --cluster-id {{j-3SD91U2E1L2QX}} --step-id {{s-3LZC0QUT43AM}}
```
Output:

```
{
    "Step": {
        "Status": {
            "Timeline": {
                "EndDateTime": "2015-06-01T19:14:30.481000-0400",
                "CreationDateTime": "2015-06-01T19:05:26.597000-0400",
                "StartDateTime": "2015-06-01T19:13:24.959000-0400"
            },
            "State": "COMPLETED",
            "StateChangeReason": {}
        },
        "Config": {
            "Args": [
                "s3://us-west-2.elasticmapreduce/libs/hive/hive-script",
                "--base-path",
                "s3://us-west-2.elasticmapreduce/libs/hive/",
                "--install-hive",
                "--hive-versions",
                "0.13.1"
            ],
            "Jar": "s3://us-west-2.elasticmapreduce/libs/script-runner/script-runner.jar",
            "Properties": {}
        },
        "Id": "s-3LZC0QUT43AM",
        "ActionOnFailure": "TERMINATE_CLUSTER",
        "Name": "Setup hive"
    }
}
```
+  For API details, see [DescribeStep](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/emr#code-examples).

```
def describe_step(cluster_id, step_id, emr_client):
    """
    Gets detailed information about the specified step, including the current state of
    the step.

    :param cluster_id: The ID of the cluster.
    :param step_id: The ID of the step.
    :param emr_client: The Boto3 EMR client object.
    :return: The retrieved information about the specified step.
    """
    try:
        response = emr_client.describe_step(ClusterId=cluster_id, StepId=step_id)
        step = response["Step"]
        logger.info("Got data for step %s.", step_id)
    except ClientError:
        logger.exception("Couldn't get data for step %s.", step_id)
        raise
    else:
        return step
```
+  For API details, see [DescribeStep](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribeStep) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        oo_result = lo_emr->describestep(
          iv_clusterid = iv_cluster_id
          iv_stepid = iv_step_id
        ).
        DATA(lo_step) = oo_result->get_step( ).
        DATA(lv_step_name) = lo_step->get_name( ).
        MESSAGE |Retrieved step information for { lv_step_name }| TYPE 'I'.
      CATCH /aws1/cx_emrinternalserverex INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
      CATCH /aws1/cx_emrinvalidrequestex INTO DATA(lo_invalid_error).
        lv_error = lo_invalid_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeStep](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------
