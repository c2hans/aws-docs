---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteContainerFleet.html
---

# DeleteContainerFleet
<a name="API_DeleteContainerFleet"></a>

 **This API works with the following fleet types:** Container

Deletes all resources and information related to a container fleet and shuts down currently running fleet instances, including those in remote locations. The container fleet must be in `ACTIVE` status to be deleted.

To delete a fleet, specify the fleet ID to be terminated. During the deletion process, the fleet status is changed to `DELETING`.

 **Learn more**

 [Setting up Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_DeleteContainerFleet_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteContainerFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DeleteContainerFleet_RequestSyntax) **   <a name="gameliftservers-DeleteContainerFleet-request-FleetId"></a>
A unique identifier for the container fleet to delete. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Elements
<a name="API_DeleteContainerFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteContainerFleet_Errors"></a>

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

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_DeleteContainerFleet_Examples"></a>

### Delete a fleet that is no longer in use
<a name="API_DeleteContainerFleet_Example_1"></a>

This example deletes an existing fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DeleteContainerFleet_Example_1_Request"></a>

```
{
    "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

#### Sample Response
<a name="API_DeleteContainerFleet_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Date: Thu, 06 Apr 2017 00:48:07 GMT
```

## See Also
<a name="API_DeleteContainerFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteContainerFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteContainerFleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
