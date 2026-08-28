---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListBuilds.html
---

# ListBuilds
<a name="API_ListBuilds"></a>

 **This API works with the following fleet types:** EC2

Retrieves build resources for all builds associated with the AWS account in use. You can limit results to builds that are in a specific status by using the `Status` parameter. Use the pagination parameters to retrieve results in

**Note**
Build resources are not listed in any particular order.

 **Learn more**

 [ Upload a Custom Server Build](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html)

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_ListBuilds_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBuilds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_ListBuilds_RequestSyntax) **   <a name="gameliftservers-ListBuilds-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListBuilds_RequestSyntax) **   <a name="gameliftservers-ListBuilds-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [Status](#API_ListBuilds_RequestSyntax) **   <a name="gameliftservers-ListBuilds-request-Status"></a>
Build status to filter results by. To retrieve all builds, leave this parameter empty.
Possible build statuses include the following:
+  **INITIALIZED** -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
+  **READY** -- The game build has been successfully uploaded. You can now create new fleets for this build.
+  **FAILED** -- The game build upload failed. You cannot create new fleets for this build.
Type: String
Valid Values: `INITIALIZED | READY | FAILED`
Required: No

## Response Syntax
<a name="API_ListBuilds_ResponseSyntax"></a>

```
{
   "Builds": [
      {
         "BuildArn": "string",
         "BuildId": "string",
         "CreationTime": number,
         "Name": "string",
         "OperatingSystem": "string",
         "ServerSdkVersion": "string",
         "SizeOnDisk": number,
         "Status": "string",
         "Version": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBuilds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Builds](#API_ListBuilds_ResponseSyntax) **   <a name="gameliftservers-ListBuilds-response-Builds"></a>
A collection of build resources that match the request.
Type: Array of [Build](API_Build.md) objects

 ** [NextToken](#API_ListBuilds_ResponseSyntax) **   <a name="gameliftservers-ListBuilds-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListBuilds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_ListBuilds_Examples"></a>

### Retrieve all builds
<a name="API_ListBuilds_Example_1"></a>

This example retrieves game server builds in the current Region. The sample request illustrates how to use the pagination parameters, `Limit` and `NextToken`, to retrieve the results in sequential sets.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListBuilds_Example_1_Request"></a>

```
{
    "Limit": 2,
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC00NDRlZjQxZS1hM2I1LTQ2NDYtODJmMy0zYzI4ZTgxNjVjEXAMPLE="
}
```

#### Sample Response
<a name="API_ListBuilds_Example_1_Response"></a>

```
{
    "Builds": [
        {"BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
            "CreationTime": 1495664528.723,
            "Name": "My_Game_Server_Build_One",
            "OperatingSystem": "WINDOWS_2022",
            "SizeOnDisk": 8567781,
            "Status": "READY",
            "Version": "12345.678"
        },
        {"BuildArn": "arn:aws:gamelift:us-west-2::build/build-3333cccc-44dd-55ee-66ff-7777aaaa88bb",
            "BuildId": "build-3333cccc-44dd-55ee-66ff-7777aaaa88bb",
            "CreationTime": 1495528748.555,
            "Name": "My_Game_Server_Build_Two",
            "OperatingSystem": "AMAZON_LINUX_2023",
            "SizeOnDisk": 8567781,
            "Status": "INITIALIZED",
            "Version": "23456.789"
        }
    ],
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjJEXAMPLE="
}
```

### Retrieve failed builds
<a name="API_ListBuilds_Example_2"></a>

This example retrieves all game server builds in the current Region that failed to upload. It uses the pagination parameters to retrieve two builds at a time. With no `NextToken` provided, this request tries to retrieve the first two results. There is only one result, so only one build resource and no `NextToken` is returned.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListBuilds_Example_2_Request"></a>

```
{
    "Limit": 2,
    "Status": "FAILED"
}
```

#### Sample Response
<a name="API_ListBuilds_Example_2_Response"></a>

```
{
    "Builds":
    [
        {"BuildArn": "arn:aws:gamelift:us-west-2::build/build-3333cccc-44dd-55ee-66ff-7777aaaa88bb",
            "BuildId": "build-3333cccc-44dd-55ee-66ff-7777aaaa88bb",
            "CreationTime": 1495528748.555,
            "Name": "My_Game_Server_Build_Two",
            "OperatingSystem": "AMAZON_LINUX_2023",
            "SizeOnDisk": 8567781,
            "Status": "FAILED",
            "Version": "23456.789"
        }
    ]
}
```

## See Also
<a name="API_ListBuilds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListBuilds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListBuilds)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
