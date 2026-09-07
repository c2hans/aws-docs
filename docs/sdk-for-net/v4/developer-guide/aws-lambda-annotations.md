---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/aws-lambda-annotations.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Using annotations to write AWS Lambda functions
<a name="aws-lambda-annotations"></a>

When writing Lambda functions, you sometimes need to write a large amount of handler code and update AWS CloudFormation templates, among other tasks. Lambda Annotations is a framework to help ease these burdens for .NET 6 Lambda functions, thereby making the experience of writing Lambda feel more natural in C\#.

As an example of the benefit of using the Lambda Annotations framework, consider the following snippets of code that add two numbers.

**Without Lambda Annotations**

```
public class Functions
{
    public APIGatewayProxyResponse LambdaMathPlus(APIGatewayProxyRequest request, ILambdaContext context)
    {
        if (!request.PathParameters.TryGetValue("x", out var xs))
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = (int)HttpStatusCode.BadRequest
            };
        }
        if (!request.PathParameters.TryGetValue("y", out var ys))
        {
            return new APIGatewayProxyResponse
            {
                StatusCode = (int)HttpStatusCode.BadRequest
            };
        }

        var x = int.Parse(xs);
        var y = int.Parse(ys);

        return new APIGatewayProxyResponse
        {
            StatusCode = (int)HttpStatusCode.OK,
            Body = (x + y).ToString(),
            Headers = new Dictionary<string, string> { { "Content-Type", "text/plain" } }
        };
    }
}
```

**With Lambda Annotations**

```
public class Functions
{
    [LambdaFunction]
    [RestApi("/plus/{x}/{y}")]
    public int Plus(int x, int y)
    {
        return x + y;
    }
}
```

As is shown in the example, Lambda Annotations can remove the need for certain boiler plate code.

For details about how to use the framework as well as additional information, see the following resources:
+ The [GitHub README](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.Annotations/README.md) for documentation on the APIs and attributes of Lambda Annotations.
+ The [blog post](https://aws.amazon.com/blogs/developer/net-lambda-annotations-framework/) for Lambda Annotations.
+ The [`Amazon.Lambda.Annotations`](https://www.nuget.org/packages/Amazon.Lambda.Annotations) NuGet package.
+ The [Photo Asset Management project](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/PhotoAssetManager) on GitHub. Specifically, see the [PamApiAnnotations](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/PhotoAssetManager/PamApiAnnotations) folder and references to Lambda Annotations in the project [README](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/dotnetv3/cross-service/PhotoAssetManager/README.md).
**Note**
The preceding example is specific to V3 of the AWS SDK for .NET. If you use the example with V4 of the SDK (the latest version), you might need to make adjustments according to the information in [Migrating to version 4](net-dg-v4.md).
