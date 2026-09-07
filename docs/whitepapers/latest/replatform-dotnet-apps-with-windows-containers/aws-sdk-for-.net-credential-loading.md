---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/aws-sdk-for-.net-credential-loading.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS SDK for .NET credential loading
<a name="aws-sdk-for-.net-credential-loading"></a>

 The AWS SDKs take the complexity out of coding by providing language-specific APIs for AWS services. One of the ways the AWS SDK for .NET helps is by seamlessly loading the IAM credentials at runtime. The AWS SDK for .NET searches for credentials in a certain order and uses the first available set for the current application. In its simplest form, credential loading is transparent, as can be seen by the following code example that lists the objects in an S3 bucket.

```
var s3Client = new AmazonS3Client();
var listRequest = new ListObjectsRequest
{
    BucketName = "SampleBucket",
};

ListObjectsResponse response = await s3Client.ListObjectsAsync(listRequest);

foreach (var item in response.S3Objects)
{
    Console.WriteLine("key = {0} size = {1}", item.Key, item.Size);
}
```

 The parameterless constructors for AWS service clients ([AmazonS3Client](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/S3/TS3Client.html) in this example) rely on the [FallbackCredentialsFactory](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Runtime/TFallbackCredentialsFactory.html) to load the credentials using a well-known [credential and profile resolution order](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/creds-assign.html) and includes support for Amazon ECS. This provides a frictionless developer experience while still ensuring credentials remain secure.

 This section covered the various IAM roles involved in a container’s lifecycle, including how to securely retrieve temporary credentials using the AWS SDK for .NET. Your security journey does not end here. Consider how to keep data secure both in transit and at rest.

## In-flight data protection using encryption
<a name="in-flight-data-protection-using-encryption"></a>

 By default, API calls to Amazon ECS travel through the public internet. To keep that traffic within the AWS global network, you can configure Amazon ECS to use an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a technology that enables you to privately access Amazon ECS APIs by using private IP addresses. PrivateLink restricts all network traffic between your VPC and Amazon ECS to the Amazon network. You don't need an internet gateway, NAT device, or virtual private gateway.

 You can [create VPC endpoints for Amazon ECS, Amazon ECS container agent, and Amazon ECS telemetry](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html#ecs-setting-up-vpc-create) in the Region where your containers are deployed. VPC endpoints currently do not support cross-Region requests, so if you have a multi-Region deployment, consider following the recommendations in the [Integrating cross VPC ECS cluster for enhanced security with AWS App Mesh](https://aws.amazon.com/blogs/containers/appmesh-integrating-cross-vpc-ecs-cluster-for-enhanced-security/) blog post. For more information on building a scalable multi-Region architecture in AWS, refer to the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf) whitepaper. If you are using Amazon ECS’ integration with Secrets Manager or Systems Manager Parameter Store for sensitive data, you will also need to [configure VPC endpoints for each of these services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html#ecs-setting-up-secrets).

 In addition to securing network traffic by restricting it to the AWS network, you can encrypt data in transit between your application and AWS services by [enforcing the use of TLS 1.2 when using the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/enforcing-tls.html). The following sections review the various approaches to using encryption in transit for applications running on Amazon ECS.

## TLS termination at the load balancer
<a name="tls-termination-at-the-load-balancer"></a>

 It’s a best practice to enforce TLS termination at the load balancer and both Application Load Balancers and Network Load Balancers [support TLS termination](https://aws.amazon.com/about-aws/whats-new/2019/01/network-load-balancer-now-supports-tls-termination/). Terminating TLS connections at the load balancer frees up your backend containers from the work of encrypting and decrypting your traffic. Your containers handle plain HTTP requests while offloading the complexity of managing HTTPS connections to the Load Balancers.

 This approach also simplifies certificate management since the certificates are now deployed to the load balancers instead of backend containers. Additionally, you can use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) at no charge to securely store, expire, rotate, and update your certificates. This process involves adding a TLS listener to your load balancer, configuring the backend container to listen on an unencrypted port, such as part 80 (HTTP), and configuring the listener on the load balancer to forward traffic to the unencrypted port used by your container. Refer to the [TLS Termination for Network Load Balancers](https://aws.amazon.com/blogs/aws/new-tls-termination-for-network-load-balancers/) blog post for more information.

![TLS termination at Application Load Balancer](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/tls-term.png)

## End-to-end encryption
<a name="end-to-end-encryption"></a>

 Terminating TLS connections at the load balancer and using HTTP on the backend may be sufficient for your application. However, if you are developing an application that needs to comply with strict external regulations, you may be required to secure all network connections. You can configure the load balancer to either pass TLS traffic through untouched (terminate TLS at container), or decrypt and re-encrypt for end-to-end encryption.

## Terminate TLS at the container level
<a name="terminate-tls-at-the-container-level"></a>

 This process involves adding an unencrypted listener to your load balancer, configuring backend containers to listen on the secure port and terminate HTTPS connections, and configuring the listener on the load balancer to forward traffic to the secure port used by the backend containers.

![TLS termination at the container level](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/tls-term-container.png)

## Decrypt and re-encrypt
<a name="decrypt-and-re-encrypt"></a>

 This process involves adding a TLS listener to your load balancer, configuring backend containers to listen on the secure port, terminate HTTPS connections, using a self-signed certificate, and configuring the listener on the load balancer to forward traffic to the secure port used by the backend containers.

![Re-encrypt traffic using self-signed certificate](https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/reencrypt-traffic.png)
