---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListScripts.html
---

# ListScripts
<a name="API_ListScripts"></a>

 **This API works with the following fleet types:** EC2

Retrieves script records for all Realtime scripts that are associated with the AWS account in use.

 **Learn more**

 [Amazon GameLift Servers Amazon GameLift Servers Realtime](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_ListScripts_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListScripts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_ListScripts_RequestSyntax) **   <a name="gameliftservers-ListScripts-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListScripts_RequestSyntax) **   <a name="gameliftservers-ListScripts-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListScripts_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Scripts": [
      {
         "CreationTime": number,
         "Name": "string",
         "NodeJsVersion": "string",
         "ScriptArn": "string",
         "ScriptId": "string",
         "SizeOnDisk": number,
         "StorageLocation": {
            "Bucket": "string",
            "Key": "string",
            "ObjectVersion": "string",
            "RoleArn": "string"
         },
         "Version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListScripts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListScripts_ResponseSyntax) **   <a name="gameliftservers-ListScripts-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1.

 ** [Scripts](#API_ListScripts_ResponseSyntax) **   <a name="gameliftservers-ListScripts-response-Scripts"></a>
A set of properties describing the requested script.
Type: Array of [Script](API_Script.md) objects

## Errors
<a name="API_ListScripts_Errors"></a>

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
<a name="API_ListScripts_Examples"></a>

### Retrieve all scripts
<a name="API_ListScripts_Example_1"></a>

This example retrieves the Realtime scripts in the current Region. The example illustrates using the pagination parameters to retrieve the results in sequential sets. This sample request uses a NextToken value that was returned in a previous `ListScripts` request. The response shows two script records; the first script was uploaded from an Amazon S3 bucket, and the second script was uploaded from a local zip file.

#### Sample Request
<a name="API_ListScripts_Example_1_Request"></a>

```
{
    "Limit": 2,
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC00NDRlZjQxZS1hM2I1LTQ2NDYtODJmMy0zYzI4ZTgxNjVjEXAMPLE="
}

CLI syntax:

aws gamelift list-scripts
    -limit 2
    -next-token "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC00NDRlZjQxZS1hM2I1LTQ2NDYtODJmMy0zYzI4ZTgxNjVjEXAMPLE="
```

#### Sample Response
<a name="API_ListScripts_Example_1_Response"></a>

```
{
    "Scripts": {
        "CreationTime": 1496708916.18,
        "Name": "My_Realtime_Script_2",
        "NodeJsVersion": "24.x",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "SizeOnDisk": 0,
        "StorageLocation": {
            "Bucket": "my_realtime_script_files",
            "Key": "myRealtimeScript.zip"
            "RoleArn": "arn:aws:iam::111122223333:role/GameLiftAccess"
            "ObjectVersion": null
        },
        "Version": "12345.678"
    },
    {
        "CreationTime": 1495528748.555,
        "Name": "My_Realtime_Script_1",
        "NodeJsVersion": "24.x",
        "ScriptArn": "arn:aws:gamelift:us-west-2::script/script-3333cccc-44dd-55ee-66ff-7777aaaa88bb",
        "ScriptId": "script-3333cccc-44dd-55ee-66ff-7777aaaa88bb",
        "SizeOnDisk": 9000,
        "StorageLocation": {
            "Bucket": "prod-gamescale-scripts-us-west-2",
            "Key": "123456789012/script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
        },
        "Version": "1.0.1"
    }
        "NextToken": "kyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjJEXAMPLE="
}
```

## See Also
<a name="API_ListScripts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListScripts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListScripts)
