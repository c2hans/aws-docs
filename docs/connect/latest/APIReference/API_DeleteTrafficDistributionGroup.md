---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html
---

# DeleteTrafficDistributionGroup
<a name="API_DeleteTrafficDistributionGroup"></a>

Deletes a traffic distribution group. This API can be called only in the Region where the traffic distribution group is created.

For more information about deleting traffic distribution groups, see [Delete traffic distribution groups](https://docs.aws.amazon.com/connect/latest/adminguide/delete-traffic-distribution-groups.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_DeleteTrafficDistributionGroup_RequestSyntax"></a>

```
DELETE /traffic-distribution-group/{{TrafficDistributionGroupId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTrafficDistributionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrafficDistributionGroupId](#API_DeleteTrafficDistributionGroup_RequestSyntax) **   <a name="connect-DeleteTrafficDistributionGroup-request-uri-TrafficDistributionGroupId"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_DeleteTrafficDistributionGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTrafficDistributionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTrafficDistributionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTrafficDistributionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceInUseException **
That resource is already in use (for example, you're trying to add a record with the same name as an existing record). If you are trying to delete a resource (for example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference from related resources and then try again.
 ** ResourceId **
The identifier for the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DeleteTrafficDistributionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteTrafficDistributionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteTrafficDistributionGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
