---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/verify-the-staged-rosbag-files.html
---

# Verify the staged rosbag files
<a name="verify-the-staged-rosbag-files"></a>

Complete the following steps to verify that the rosbag files are staged.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/home?).

1. Choose the bucket with a name similar to `addf-aws-solutions-raw-bucket-` {{<hash>}} `/rosbag-scene-detection/test-vehicle-01/072021/small1_2020-11-19-16-21-22_4.bag`.

1. There should be two .bag files in the bucket. These are the files we will pass to the DAG.

   If the files aren’t in the bucket, run the following CLI commands to stage the files. Replace {{<hash>}} with the unique numbering for the S3 bucket.

   ```
   $ aws s3 cp s3://proserve-blocks-datasets-us-east-1/rosbag/test-vehicle-01/072021/small1__2020-11-19-16-21-22_4.bag \
   s3://addf-aws-solutions-raw-bucket-<hash>/rosbag-scene-detection/test-vehicle-01/072021/small1__2020-11-19-16-21-22_4.bag
   ```

```
$ aws s3 cp s3://proserve-blocks-datasets-us-east-1/rosbag/test-vehicle-01/072021/small2__2020-11-19-16-21-22_4.bag \
s3://addf-aws-solutions-raw-bucket-<hash>/rosbag-scene-detection/test-vehicle-02/072021/small2__2020-11-19-16-21-22_4.bag
```
