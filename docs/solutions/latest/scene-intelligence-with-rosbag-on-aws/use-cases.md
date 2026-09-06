---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/use-cases.html
---

# Use cases
<a name="use-cases"></a>

 **Extract rosbag data**

You can use this solution to extract the structured data (metadata) and unstructured data, such as images, from defined topics in Robot Operating System (ROS)1 rosbag files. The topics in this solution match the same that rosbag provides, and you can change them to fit your custom topics. The solution writes all topic data to Amazon S3, including images as .png files and metadata as Apache Parquet.

 **Apply business logic**

You can apply custom business logic to the extracted data by using an Apache Spark script. Modify the processing DAG to match your rosbag, apply your own logic, or use the provided DAG and scripts.

 **Search for anomalies**

The processing logic output applied to the extracted data is written to DynamoDB and OpenSearch Service. You can query the metadata output from an OpenSearch Service dashboard or with an OpenSearch service application programming interface (API) to locate a section of the rosbag file for inspection.
