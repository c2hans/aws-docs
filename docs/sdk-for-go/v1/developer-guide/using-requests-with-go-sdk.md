---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-requests-with-go-sdk.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# AWS SDK for Go Request Examples
<a name="using-requests-with-go-sdk"></a>

The AWS SDK for Go examples can help you write your own applications. The examples assume you have already set up and configured the SDK (that is, you have imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](setting-up.md) and [Configuring the AWS SDK for Go](configuring-sdk.md).

## Using context.Context with SDK Requests
<a name="using-context-context-with-requests"></a>

In Go 1.7, the `context.Context` type was added to `http.Request`. This type provides an easy way to implement deadlines and cancellations on requests.

To use this pattern with the SDK, call `WithContext` on the `HTTPRequest` field of the SDK’s `request.Request` type, and provide your `Context value`. The following example highlights this process with a timeout on Amazon SQS`ReceiveMessage`.

```
req, resp := svc.ReceiveMessageRequest(params)
req.HTTPRequest = req.HTTPRequest.WithContext(ctx)

err := req.Send()
if err != nil {
    fmt.Println("Got error receiving message:")
    fmt.Println(err.Error())
} else {
    fmt.Println(resp)
}
```

## Using API Field Setters with SDK Requests
<a name="using-api-field-setters"></a>

In addition to setting API parameters by using struct fields, you can also use chainable setters on the API operation parameter fields. This enables you to use a chain of setters to set the fields of the API struct.

```
svc := s3.New(sess)

_, err := svc.PutObject((&s3.PutObjectInput{}).
    SetBucket(*bucket).
    SetKey(*key).
    SetBody(strings.NewReader("object body")), //.
//      SetWebsiteRedirectLocation("https://example.com/something"),
)
```

You can also use this pattern with nested fields in API operation requests.

```
resp, err := svc.UpdateService((&ecs.UpdateServiceInput{}).
    SetService("myService").
    SetDeploymentConfiguration((&ecs.DeploymentConfiguration{}).
        SetMinimumHealthyPercent(80),
    ),
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
