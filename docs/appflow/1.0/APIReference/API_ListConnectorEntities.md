---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ListConnectorEntities.html
---

# ListConnectorEntities
<a name="API_ListConnectorEntities"></a>

 Returns the list of available connector entities supported by Amazon AppFlow. For example, you can query Salesforce for *Account* and *Opportunity* entities, or query ServiceNow for the *Incident* entity.

## Request Syntax
<a name="API_ListConnectorEntities_RequestSyntax"></a>

```
POST /list-connector-entities HTTP/1.1
Content-type: application/json

{
   "apiVersion": "{{string}}",
   "connectorProfileName": "{{string}}",
   "connectorType": "{{string}}",
   "entitiesPath": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConnectorEntities_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectorEntities_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [apiVersion](#API_ListConnectorEntities_RequestSyntax) **   <a name="appflow-ListConnectorEntities-request-apiVersion"></a>
The version of the API that's used by the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** [connectorProfileName](#API_ListConnectorEntities_RequestSyntax) **   <a name="appflow-ListConnectorEntities-request-connectorProfileName"></a>
 The name of the connector profile. The name is unique for each `ConnectorProfile` in the AWS account, and is used to query the downstream connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

 ** [connectorType](#API_ListConnectorEntities_RequestSyntax) **   <a name="appflow-ListConnectorEntities-request-connectorType"></a>
 The type of connector, such as Salesforce, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** [entitiesPath](#API_ListConnectorEntities_RequestSyntax) **   <a name="appflow-ListConnectorEntities-request-entitiesPath"></a>
 This optional parameter is specific to connector implementation. Some connectors support multiple levels or categories of entities. You can find out the list of roots for such providers by sending a request without the `entitiesPath` parameter. If the connector supports entities at different roots, this initial request returns the list of roots. Otherwise, this request returns all entities supported by the provider.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\s\w/!@#+=,.-]*`
Required: No

 ** [maxResults](#API_ListConnectorEntities_RequestSyntax) **   <a name="appflow-ListConnectorEntities-request-maxResults"></a>
The maximum number of items that the operation returns in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [nextToken](#API_ListConnectorEntities_RequestSyntax) **   <a name="appflow-ListConnectorEntities-request-nextToken"></a>
A token that was provided by your prior `ListConnectorEntities` operation if the response was too big for the page size. You specify this token to get the next page of results in paginated response.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_ListConnectorEntities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "connectorEntityMap": {
      "string" : [
         {
            "hasNestedEntities": boolean,
            "label": "string",
            "name": "string"
         }
      ]
   },
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectorEntities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectorEntityMap](#API_ListConnectorEntities_ResponseSyntax) **   <a name="appflow-ListConnectorEntities-response-connectorEntityMap"></a>
 The response of `ListConnectorEntities` lists entities grouped by category. This map's key represents the group name, and its value contains the list of entities belonging to that group.
Type: String to array of [ConnectorEntity](API_ConnectorEntity.md) objects map
Key Length Constraints: Maximum length of 128.
Key Pattern: `\S+`

 ** [nextToken](#API_ListConnectorEntities_ResponseSyntax) **   <a name="appflow-ListConnectorEntities-response-nextToken"></a>
A token that you specify in your next `ListConnectorEntities` operation to get the next page of results in paginated response. The `ListConnectorEntities` operation provides this token if the response is too big for the page size.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`

## Errors
<a name="API_ListConnectorEntities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConnectorAuthenticationException **
 An error occurred when authenticating with the connector endpoint.
HTTP Status Code: 401

 ** ConnectorServerException **
 An error occurred when retrieving data from the connector endpoint.
HTTP Status Code: 400

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ListConnectorEntities_Examples"></a>

### ListConnectorEntities example
<a name="API_ListConnectorEntities_Example_1"></a>

This example shows sample requests and a sample response for the `ListConnectorEntities` API. The second sample request shows a request without the optional `connectorType`).

#### Sample Request
<a name="API_ListConnectorEntities_Example_1_Request"></a>

```
{
  "connectorType": "Slack",
  "connectorProfileName": "vmSlackProfile"
}
```

#### Sample Request
<a name="API_ListConnectorEntities_Example_1_Request"></a>

```
{
  "connectorProfileName": "vmSlackProfile"
}
```

#### Sample Response
<a name="API_ListConnectorEntities_Example_1_Response"></a>

```
{
  "connectorEntityMap":
  {
    "Objects":
    [
        {"hasNestedEntities": true,
        "label": "Conversations","name": "conversations"}
    ]
  }
}
```

#### Sample Request
<a name="API_ListConnectorEntities_Example_1_Request"></a>

```
{
  "connectorProfileName": "vmSlackProfile",
  "connectorType": "Slack",
  "entitiesPath": "conversations"
}
```

#### Sample Response
<a name="API_ListConnectorEntities_Example_1_Response"></a>

```
{
  "connectorEntityMap":
  {
    "Channels": [
      {
        "hasNestedEntities": false,
        "label": "new-to-slack",
        "name": "conversations/CQCFDC534"
      },
      {
        "hasNestedEntities": false,
        "label": "advising",
        "name": "conversations/CQDSNS2AX"
      },
      {
        "hasNestedEntities": false,
        "label": "general",
        "name": "conversations/CQTFBK48N"
      },
      {
        "hasNestedEntities": false,
        "label": "random",
        "name": "conversations/CQTFBK6CE"
      },
      {
        "hasNestedEntities": false,
        "label": "investing",
        "name": "conversations/CQTFBKDT8"
      },
      {
        "hasNestedEntities": false,
        "label": "memories",
        "name": "conversations/CS44VCEC9"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-nyc",
        "name": "conversations/CV84P3D7A"
      },
      {
        "hasNestedEntities": false,
        "label": "marketing",
        "name": "conversations/C012DDQRU95"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-phi",
        "name": "conversations/C012DTFRBL7"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-philadelphia",
        "name": "conversations/C012N003VU6"
      },
      {
        "hasNestedEntities": false,
        "label": "lol",
        "name": "conversations/C012NJTMZEJ"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-atlanta",
        "name": "conversations/C012P2739BQ"
      },
      {
        "hasNestedEntities": false,
        "label": "it-support",
        "name": "conversations/C012SRQMLRH"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-nashville",
        "name": "conversations/C012U9TM5DZ"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-texas",
        "name": "conversations/C012VHLB63X"
      },
      {
        "hasNestedEntities": false,
        "label": "data",
        "name": "conversations/C012Z3VMA7N"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-san-francisco",
        "name": "conversations/C01308U07HA"
      },
      {
        "hasNestedEntities": false,
        "label": "slack-feedback",
        "name": "conversations/C0131PCV93N"
      },
      {
        "hasNestedEntities": false,
        "label": "home-of-seattle",
        "name": "conversations/C0136MRRQHX"
      },
      {
        "hasNestedEntities": false,
        "label": "operations",
        "name": "conversations/C0136QPJ1KK"
      },
      {
        "hasNestedEntities": false,
        "label": "product",
        "name": "conversations/C0137S730KT"
      },
      {
        "hasNestedEntities": false,
        "label": "dev",
        "name": "conversations/C013HUHSRGQ"
      },
      {
        "hasNestedEntities": false,
        "label": "infra",
        "name": "conversations/C013KP5TQ2J"
      },
      {
        "hasNestedEntities": false,
        "label": "pets",
        "name": "conversations/C013NTC2L0G"
      },
      {
        "hasNestedEntities": false,
        "label": "founders",
        "name": "conversations/C014M9JBWCU"
      }
    ]
  }
}
```

## See Also
<a name="API_ListConnectorEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/ListConnectorEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ListConnectorEntities)
