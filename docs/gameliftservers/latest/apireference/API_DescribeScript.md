---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeScript.html
---

# DescribeScript
<a name="API_DescribeScript"></a>

 **This API works with the following fleet types:** EC2

Retrieves properties for a Realtime script.

To request a script record, specify the script ID. If successful, an object containing the script properties is returned.

 **Learn more**

 [Amazon GameLift Servers Amazon GameLift Servers Realtime](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribeScript_RequestSyntax"></a>

```
{
   "ScriptId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeScript_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ScriptId](#API_DescribeScript_RequestSyntax) **   <a name="gameliftservers-DescribeScript-request-ScriptId"></a>
A unique identifier for the Realtime script to retrieve properties for. You can use either the script ID or ARN value.
Type: String
Pattern: `^script-\S+|^arn:.*:script\/script-\S+`
Required: Yes

## Response Syntax
<a name="API_DescribeScript_ResponseSyntax"></a>

```
{
   "Script": {
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
}
```

## Response Elements
<a name="API_DescribeScript_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Script](#API_DescribeScript_ResponseSyntax) **   <a name="gameliftservers-DescribeScript-response-Script"></a>
A set of properties describing the requested script.
Type: [Script](API_Script.md) object

## Errors
<a name="API_DescribeScript_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_DescribeScript_Examples"></a>

### View a script record
<a name="API_DescribeScript_Example_1"></a>

This example illustrates one usage of DescribeScript.

#### Sample Request
<a name="API_DescribeScript_Example_1_Request"></a>

```
{
        "ScriptId": "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
}

CLI syntax:

aws gamelift describe-script --script-id "script-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
```

#### Sample Response
<a name="API_DescribeScript_Example_1_Response"></a>

```
{
    "Script": {
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
    }
}
```

## See Also
<a name="API_DescribeScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeScript)
