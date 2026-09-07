---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/invoke-the-dag.html
---

# Invoke the DAG
<a name="invoke-the-dag"></a>

Complete the following steps to invoke the DAG.

1. Sign in to the [Amazon MWAA console](https://console.aws.amazon.com/mwaa).

1. Select **Environments** from the navigation menu.

1. Select `addf-aws-solutions-core-mwaa-environment` and choose **Open Airflow UI**. This opens a new window to the Airflow DAG.

    **Example Airflow environments screen listing addf-aws-solutions-core-mwaa-environment and Open Airflow UI link.**
![airflow dag](https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/airflow-dag.png)

1. Choose the `vsi-image-pipeline` DAG.

1. Choose **Play** and select **Trigger DAG w/ config**.

    **Example vsi\_image\_pipeline screen with Trigger Dag w/ config option in upper right corner.**
![vsi image pipeline](https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/vsi-image-pipeline.png)

1. Provide the paths to the staged rosbag files. The following is an example, where you replace {{<vehicle-name>}} with the vehicle name, {{<bucket>}} with the S3 bucket name, and {{<prefix-to-dag>}} with your prefix:

   ```
   {
    "drives_to_process": {
    "<vehicle-name>": {
    "bucket": "<bucket>",
    "prefix": "rosbag-scene-detection/test-vehicle-02/072021/ "
    },
    "<vehicle-name>": {
    "bucket": "<bucket>",
    "prefix": "<prefix-to-dag>"
    }
    }
   }
   ```
**Note**
The solution requires a minimum of two rosbag entries to invoke the DAG.

The following is an example with these fields completed, where the vehicle names are `test-vehicle-01` and `test-vehicle-02`, the bucket name is `addf-aws-solutions-raw-bucket-123456`, and the prefix is `rosbag-scene-detection/test-vehicle-01/072021/`:

```
{
 "drives_to_process": {
 "test-vehicle-01": {
 "bucket": "addf-aws-solutions-raw-bucket-123456",
 "prefix": "rosbag-scene-detection/test-vehicle-01/072021/"
 },
 "test-vehicle-02": {
 "bucket": "addf-aws-solutions-raw-bucket-123456",
 "prefix": "rosbag-scene-detection/test-vehicle-02/072021/"
 }
 }
}
```

The following image shows the previous example code in the Airflow DAG window:

 **Example vsi\_image\_pipeline screen displaying previous sample code and Trigger button.**

![vsi image pipeline trigger](https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/vsi-image-pipeline-trigger.png)

1. Choose **Trigger**. Wait for the DAG to complete running (approximately 20 minutes).
