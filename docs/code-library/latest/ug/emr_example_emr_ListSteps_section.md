---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/emr_example_emr_ListSteps_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListSteps` with an AWS SDK or CLI
<a name="emr_example_emr_ListSteps_section"></a>

The following code examples show how to use `ListSteps`.

------
#### [ CLI ]

**AWS CLI**
**To list the steps in a cluster**
The following `list-steps` example lists all of the steps in a cluster with the cluster ID `j-3SD91U2E1L2QX`.

```
aws emr list-steps \
    --cluster-id {{j-3SD91U2E1L2QX}}
```
Output:

```
{
    "Steps": [
        {
            "Id": "s-2BRWVHXA3EXBT",
            "Name": "Custom JAR",
            "Config": {
                "Jar": "s3://amzn-s3-demo-bucket/mytest.jar",
                "Properties": {},
                "MainClass": "mymainclass",
                "Args": [
                    "arg1",
                    "arg2"
                ]
            },
            "ActionOnFailure": "CONTINUE",
            "Status": {
                "State": "COMPLETED",
                "StateChangeReason": {},
                "Timeline": {
                    "CreationDateTime": "2024-05-14T18:07:31.123000+00:00",
                    "StartDateTime": "2024-05-14T18:10:45.456000+00:00",
                    "EndDateTime": "2024-05-14T18:12:20.789000+00:00"
                }
            }
        },
        {
            "Id": "s-1AXF2SNQKPLZR",
            "Name": "Setup Hadoop Debugging",
            "Config": {
                "Jar": "command-runner.jar",
                "Properties": {},
                "Args": [
                    "state-pusher-script"
                ]
            },
            "ActionOnFailure": "TERMINATE_CLUSTER",
            "Status": {
                "State": "COMPLETED",
                "StateChangeReason": {},
                "Timeline": {
                    "CreationDateTime": "2024-05-14T18:01:02.345000+00:00",
                    "StartDateTime": "2024-05-14T18:09:30.678000+00:00",
                    "EndDateTime": "2024-05-14T18:10:40.901000+00:00"
                }
            }
        }
    ]
}
```
For more information, see [Submit work to an Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-work-with-steps.html) in the *Amazon EMR Management Guide*.
+  For API details, see [ListSteps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-steps.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/emr#code-examples).

```
def list_steps(cluster_id, emr_client):
    """
    Gets a list of steps for the specified cluster. In this example, all steps are
    returned, including completed and failed steps.

    :param cluster_id: The ID of the cluster.
    :param emr_client: The Boto3 EMR client object.
    :return: The list of steps for the specified cluster.
    """
    try:
        response = emr_client.list_steps(ClusterId=cluster_id)
        steps = response["Steps"]
        logger.info("Got %s steps for cluster %s.", len(steps), cluster_id)
    except ClientError:
        logger.exception("Couldn't get steps for cluster %s.", cluster_id)
        raise
    else:
        return steps
```
+  For API details, see [ListSteps](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListSteps) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        oo_result = lo_emr->liststeps(
          iv_clusterid = iv_cluster_id
        ).
        DATA(lt_steps) = oo_result->get_steps( ).
        DATA(lv_step_count) = lines( lt_steps ).
        MESSAGE |Retrieved { lv_step_count } steps for cluster| TYPE 'I'.
      CATCH /aws1/cx_emrinternalserverex INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
      CATCH /aws1/cx_emrinvalidrequestex INTO DATA(lo_invalid_error).
        lv_error = lo_invalid_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListSteps](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------
