---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListConnectors.html
---

# ListConnectors
<a name="API_ListConnectors"></a>

Returns the list of all registered custom connectors in your AWS account. This API lists only custom connectors registered in this account, not the AWS authored connectors.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
POST /list-connectors HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListConnectors_RequestSyntax) **   <a name="appflow-ListConnectors-request-maxResults"></a>
Specifies the maximum number of items that should be returned in the result set. The default for `maxResults` is 20 (for all paginated API operations).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListConnectors_RequestSyntax) **   <a name="appflow-ListConnectors-request-nextToken"></a>
The pagination token for the next page of data.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectors": [
      {
         "applicationType": "string",
         "connectorDescription": "string",
         "connectorLabel": "string",
         "connectorModes": [ "string" ],
         "connectorName": "string",
         "connectorOwner": "string",
         "connectorProvisioningType": "string",
         "connectorType": "string",
         "connectorVersion": "string",
         "registeredAt": number,
         "registeredBy": "string",
         "supportedDataTransferTypes": [ "string" ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectors](#API_ListConnectors_ResponseSyntax) **   <a name="appflow-ListConnectors-response-connectors"></a>
Contains information about the connectors supported by Amazon AppFlow.
Type: Array of [ConnectorDetail](API_ConnectorDetail.md) objects

 ** [nextToken](#API_ListConnectors_ResponseSyntax) **   <a name="appflow-ListConnectors-response-nextToken"></a>
The pagination token for the next page of data. If nextToken=null, this means that all records have been fetched.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_ListConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ListConnectors_Examples"></a>

### Listing connectors
<a name="API_ListConnectors_Example_1"></a>

This example shows a sample request for the `ListConnector` API and a sample response.

#### Sample Request
<a name="API_ListConnectors_Example_1_Request"></a>

```
{
  "maxResults": 1,
  "nextToken": "nextToken_value"
}
```

#### Sample Response
<a name="API_ListConnectors_Example_1_Response"></a>

```
{
  "connectors":
  [
    {
      "connectorArn": "Arn of connector1",
      "connectorDescription": "Some Sample Connector1",
      "connectorName": "Salesforce custom connector1",
      "connectorOwner": "AppFlow",
      "connectorVersion": "1.0",
      "applicationType": "Salesforce",
      "connectorType": "CUSTOMCONNECTOR",
      "connectorLabel": "MyCustomConnector",
      "registeredAt": 1628732168.132,
      "registeredBy": "CUSTOM",
      "tags": null,
      "connectorModes":
      [
        "SOURCE",
        "DESTINATION"
      ],
      "connectorProvisioningType": "LAMBDA"
    },
    {
      "connectorArn": "Arn of connector2",
      "connectorDescription": "Some Sample Connector2",
      "connectorName": "Salesforce custom connector2",
      "connectorOwner": "AppFlow",
      "connectorVersion": "1.0",
      "applicationType": "Salesforce",
      "connectorType": "CUSTOMCONNECTOR",
      "connectorLabel": "MyCustomConnector",
      "registeredAt": 1628732168.132,
      "registeredBy": "CUSTOM",
      "tags": null,
      "connectorModes":
      [
        "SOURCE",
        "DESTINATION"
      ],
      "connectorProvisioningType": "LAMBDA"
    }
  ],
  "nextToken": null
}
```

## See Also
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/ListConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ListConnectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
