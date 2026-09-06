---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/sdk-utilities-ec2-imds.html
---

# Amazon EC2 Instance Metadata Service
<a name="sdk-utilities-ec2-imds"></a>

 You can use the AWS SDK for Go to access the [Amazon EC2 Instance Metadata Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html). The [feature/ec2/imds](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/ec2/imds) Go package provides a [Client](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/feature/ec2/imds#Client) type that can be used to access the Amazon EC2 Instance Metadata Service. The `Client` and associated operations can be used similar to the other AWS service clients provided by the SDK. To learn more information on how to configure the SDK, and use service clients see [Configure the SDK](configure-gosdk.md) and [Use the AWS SDK for Go v2 with AWS services](use-services.md).

 The client can help you easily retrieve information about instances on which your applications run, such as its AWS Region or local IP address. Typically, you must create and submit HTTP requests to retrieve instance metadata. Instead, create an `imds.Client` to access the Amazon EC2 Instance Metadata Service using a programmatic client like other AWS Services.

 For example to construct a client:

```
import "context"
import "github.com/aws/aws-sdk-go-v2/config"
import "github.com/aws/aws-sdk-go-v2/feature/ec2/imds"

// ...

cfg, err := config.LoadDefaultConfig(context.TODO())
if err != nil {
    log.Printf("error: %v", err)
    return
}

client := imds.NewFromConfig(cfg)
```

 Then use the service client to retrieve information from a metadata category such as `local-ipv4` (the private IP address of the instance).

```
localIp, err := client.GetMetadata(context.TODO(), &imds.GetMetadataInput{
    Path: "local-ipv4",
})
if err != nil {
    log.Printf("Unable to retrieve the private IP address from the EC2 instance: %s\n", err)
    return
}
content, _ := io.ReadAll(localIp.Content)
fmt.Printf("local-ip: %v\n", string(content))
```

 For a list of all metadata categories, see [Instance metadata categories](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-categories) in the Amazon EC2 User Guide.
