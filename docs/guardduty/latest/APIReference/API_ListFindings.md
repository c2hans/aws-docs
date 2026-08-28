---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListFindings.html
---

# ListFindings
<a name="API_ListFindings"></a>

Lists GuardDuty findings for the specified detector ID.

There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_ListFindings_RequestSyntax"></a>

```
POST /detector/{{DetectorId}}/findings HTTP/1.1
Content-type: application/json

{
   "findingCriteria": {
      "criterion": {
         "{{string}}" : {
            "eq": [ "{{string}}" ],
            "equals": [ "{{string}}" ],
            "greaterThan": {{number}},
            "greaterThanOrEqual": {{number}},
            "gt": {{number}},
            "gte": {{number}},
            "lessThan": {{number}},
            "lessThanOrEqual": {{number}},
            "lt": {{number}},
            "lte": {{number}},
            "matches": [ "{{string}}" ],
            "neq": [ "{{string}}" ],
            "notEquals": [ "{{string}}" ],
            "notMatches": [ "{{string}}" ]
         }
      }
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortCriteria": {
      "attributeName": "{{string}}",
      "orderBy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListFindings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_ListFindings_RequestSyntax) **   <a name="guardduty-ListFindings-request-uri-DetectorId"></a>
The ID of the detector that specifies the GuardDuty service whose findings you want to list.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Request Body
<a name="API_ListFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [findingCriteria](#API_ListFindings_RequestSyntax) **   <a name="guardduty-ListFindings-request-findingCriteria"></a>
Represents the criteria used for querying findings. Valid values include:
+ JSON field name
+ accountId
+ region
+ confidence
+ id
+ resource.accessKeyDetails.accessKeyId
+ resource.accessKeyDetails.principalId
+ resource.accessKeyDetails.userName
+ resource.accessKeyDetails.userType
+ resource.instanceDetails.iamInstanceProfile.id
+ resource.instanceDetails.imageId
+ resource.instanceDetails.instanceId
+ resource.instanceDetails.networkInterfaces.ipv6Addresses
+ resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress
+ resource.instanceDetails.networkInterfaces.publicDnsName
+ resource.instanceDetails.networkInterfaces.publicIp
+ resource.instanceDetails.networkInterfaces.securityGroups.groupId
+ resource.instanceDetails.networkInterfaces.securityGroups.groupName
+ resource.instanceDetails.networkInterfaces.subnetId
+ resource.instanceDetails.networkInterfaces.vpcId
+ resource.instanceDetails.tags.key
+ resource.instanceDetails.tags.value
+ resource.resourceType
+ service.action.actionType
+ service.action.awsApiCallAction.api
+ service.action.awsApiCallAction.callerType
+ service.action.awsApiCallAction.remoteIpDetails.city.cityName
+ service.action.awsApiCallAction.remoteIpDetails.country.countryName
+ service.action.awsApiCallAction.remoteIpDetails.ipAddressV4
+ service.action.awsApiCallAction.remoteIpDetails.organization.asn
+ service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg
+ service.action.awsApiCallAction.serviceName
+ service.action.dnsRequestAction.domain
+ service.action.dnsRequestAction.domainWithSuffix
+ service.action.networkConnectionAction.blocked
+ service.action.networkConnectionAction.connectionDirection
+ service.action.networkConnectionAction.localPortDetails.port
+ service.action.networkConnectionAction.protocol
+ service.action.networkConnectionAction.remoteIpDetails.country.countryName
+ service.action.networkConnectionAction.remoteIpDetails.ipAddressV4
+ service.action.networkConnectionAction.remoteIpDetails.organization.asn
+ service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg
+ service.action.networkConnectionAction.remotePortDetails.port
+ service.additionalInfo.threatListName
+ service.archived

  When this attribute is set to 'true', only archived findings are listed. When it's set to 'false', only unarchived findings are listed. When this attribute is not set, all existing findings are listed.
+ service.ebsVolumeScanDetails.scanId
+ service.resourceRole
+ severity
+ type
+ updatedAt

  Type: Timestamp in Unix Epoch millisecond format: 1486685375000
Type: [FindingCriteria](API_FindingCriteria.md) object
Required: No

 ** [maxResults](#API_ListFindings_RequestSyntax) **   <a name="guardduty-ListFindings-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListFindings_RequestSyntax) **   <a name="guardduty-ListFindings-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
Type: String
Required: No

 ** [sortCriteria](#API_ListFindings_RequestSyntax) **   <a name="guardduty-ListFindings-request-sortCriteria"></a>
Represents the criteria used for sorting findings.
Type: [SortCriteria](API_SortCriteria.md) object
Required: No

## Response Syntax
<a name="API_ListFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingIds": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingIds](#API_ListFindings_ResponseSyntax) **   <a name="guardduty-ListFindings-response-findingIds"></a>
The IDs of the findings that you're listing.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [nextToken](#API_ListFindings_ResponseSyntax) **   <a name="guardduty-ListFindings-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String

## Errors
<a name="API_ListFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_ListFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
