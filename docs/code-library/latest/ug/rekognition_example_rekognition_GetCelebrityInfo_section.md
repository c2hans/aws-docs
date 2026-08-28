---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/rekognition_example_rekognition_GetCelebrityInfo_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetCelebrityInfo` with an AWS SDK or CLI
<a name="rekognition_example_rekognition_GetCelebrityInfo_section"></a>

The following code examples show how to use `GetCelebrityInfo`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Rekognition/#code-examples).

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Rekognition;
    using Amazon.Rekognition.Model;

    /// <summary>
    /// Shows how to use Amazon Rekognition to retrieve information about the
    /// celebrity identified by the supplied celebrity Id.
    /// </summary>
    public class CelebrityInfo
    {
        public static async Task Main()
        {
            string celebId = "nnnnnnnn";

            var rekognitionClient = new AmazonRekognitionClient();

            var celebrityInfoRequest = new GetCelebrityInfoRequest
            {
                Id = celebId,
            };

            Console.WriteLine($"Getting information for celebrity: {celebId}");

            var celebrityInfoResponse = await rekognitionClient.GetCelebrityInfoAsync(celebrityInfoRequest);

            // Display celebrity information.
            Console.WriteLine($"celebrity name: {celebrityInfoResponse.Name}");
            Console.WriteLine("Further information (if available):");
            celebrityInfoResponse.Urls.ForEach(url =>
            {
                Console.WriteLine(url);
            });
        }
    }
```
+  For API details, see [GetCelebrityInfo](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityInfo) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To get information about a celebrity**
The following `get-celebrity-info` command displays information about the specified celebrity. The `id` parameter comes from a previous call to `recognize-celebrities`.

```
aws rekognition get-celebrity-info --id {{nnnnnnn}}
```
Output:

```
{
    "Name": "Celeb A",
    "Urls": [
        "www.imdb.com/name/aaaaaaaaa"
    ]
}
```
For more information, see [Getting Information About a Celebrity](https://docs.aws.amazon.com/rekognition/latest/dg/get-celebrity-info-procedure.html) in the *Amazon Rekognition Developer Guide*.
+  For API details, see [GetCelebrityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/get-celebrity-info.html) in *AWS CLI Command Reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
