---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/appendix-a-getting-the-availability-zone-id.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix A – Getting the Availability Zone ID
<a name="appendix-a-getting-the-availability-zone-id"></a>

 If you are using the AWS .NET SDK (as well as some others like JavaScript) or running your system on an EC2 instance (including Amazon ECS and Amazon EKS), you can get the Availability Zone ID directly.
+  **AWS .NET SDK**

  ```
  Amazon.Util.EC2InstanceMetadata.GetData(“/placement/availability-zone-id”)
  ```
+  **EC2 Instance Metadata Service**

  ```
  curl http://169.254.169.254/latest/meta-data/placement/availability-zone-id
  ```

   On other platforms, such as Lambda and Fargate, you will need to retrieve the Availability Zone name and then find the mapping to the Availability Zone ID. With the Availability Zone name you can find the Availability Zone ID like this:

  ```
  aws ec2 describe-availability-zones --zone-names $AZ --output json
      --query ‘AvailabilityZones[0].ZoneId’
  ```

   The following examples to find the Availability Zone name to be used in the example above are written in bash using the AWS CLI and the package [jq](https://stedolan.github.io/jq/). They will need to be converted to the programming language used for your workload.
  +  **Amazon ECS** - If the Instance Metadata Service (IMDS) is blocked by the host, you can use the container metadata file instead.

    ```
    AZ=$(cat $ECS_CONTAINER_METADATA_FILE | jq –-raw-output
        .AvailabilityZone)
    ```
  +  **Fargate** (platform version 1.4 or later)

    ```
    AZ=$(curl $ECS_CONTAINER_METADATA_URI_V4/task | jq --raw-output
        .AvailabilityZone)
    ```
  +  **Lambda** – The Availability Zone is not exposed directly to the function. To find it, you need to complete several steps. To do this, you will need to build a private API Gateway REST endpoint that returns the IP address of the requestor. This will identify the private IP assigned to the elastic network interface being used by the function.
    +  Call the Lambda `GetFunction` API to find the VPC ID of the function.
    +  Call the API Gateway service to get the function’s IP.
    +  Using the IP and VPC ID, find the associated network interface and extract the Availability Zone.

    ```
    VPC_ID=$(aws lambda get-function --function-name $ AWS_LAMBDA_FUNCTION_NAME --region $AWS_REGION --output json --query ‘Configuration.VpcConfig.VpcId’)

    MY_IP=$(curl http://whats-my-private-ip.internal)

    AZ=$(aws ec2 describe-network-interfaces --filters Name=private-ip-address,Values=$MY_IP Name=vpc-id,Values=$VPC_ID --region $AWS_REGION --output json –query ‘NetworkInterfaces[0].AvailabilityZone’)
    ```
