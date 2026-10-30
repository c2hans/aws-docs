---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CompareDomainConfiguration.html
---

# CompareDomainConfiguration
<a name="API_CompareDomainConfiguration"></a>

Compares the metadata of two domains and reports where they differ. Use this operation to check that a secondary domain is configured consistently with its primary before you rely on it, because replication copies index data but does not copy domain metadata such as index templates, ingest pipelines, or security roles.

You choose which categories to compare. The response reports, for each category, how many items match, how many exist on only one domain, and which fields diverge.

## Request Syntax
<a name="API_CompareDomainConfiguration_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/compareDomainConfiguration HTTP/1.1
Content-type: application/json

{
   "Categories": [ "{{string}}" ],
   "SourceDomainArn": "{{string}}",
   "TargetDomainArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CompareDomainConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CompareDomainConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Categories](#API_CompareDomainConfiguration_RequestSyntax) **   <a name="opensearchservice-CompareDomainConfiguration-request-Categories"></a>
The metadata categories to compare. At least one is required, and only the categories you name are read and returned.
+  `aliases`
+  `alerting_monitors`
+  `cluster_settings`
+  `component_templates`
+  `ingest_pipelines`
+  `ism_policies` — index state management policies
+  `security_action_groups`
+  `security_internal_users`
+  `security_role_mappings`
+  `security_roles`
+  `templates` — index templates
The set of categories grows over time, so this list is not fixed. A category the service does not recognise is rejected with the supported categories named in the error message.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [SourceDomainArn](#API_CompareDomainConfiguration_RequestSyntax) **   <a name="opensearchservice-CompareDomainConfiguration-request-SourceDomainArn"></a>
The Amazon Resource Name (ARN) of the domain to compare from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: Yes

 ** [TargetDomainArn](#API_CompareDomainConfiguration_RequestSyntax) **   <a name="opensearchservice-CompareDomainConfiguration-request-TargetDomainArn"></a>
The Amazon Resource Name (ARN) of the domain to compare against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_CompareDomainConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Categories": {
      "string" : {
         "Diverged": number,
         "InSync": number,
         "Items": {
            "Diverged": [
               {
                  "Fields": [
                     {
                        "Path": "string",
                        "Policy": "string",
                        "SourceValue": "string",
                        "TargetValue": "string"
                     }
                  ],
                  "Name": "string"
               }
            ],
            "SourceOnly": [ "string" ],
            "TargetOnly": [ "string" ]
         },
         "SourceOnly": number,
         "Status": "string",
         "TargetOnly": number,
         "Truncated": boolean
      }
   },
   "SourceDomainArn": "string",
   "TargetDomainArn": "string"
}
```

## Response Elements
<a name="API_CompareDomainConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Categories](#API_CompareDomainConfiguration_ResponseSyntax) **   <a name="opensearchservice-CompareDomainConfiguration-response-Categories"></a>
The comparison result for each category you requested, keyed by category name.
Type: String to [CategoryDiffResult](API_CategoryDiffResult.md) object map
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [SourceDomainArn](#API_CompareDomainConfiguration_ResponseSyntax) **   <a name="opensearchservice-CompareDomainConfiguration-response-SourceDomainArn"></a>
The Amazon Resource Name (ARN) of the domain that was compared from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`

 ** [TargetDomainArn](#API_CompareDomainConfiguration_ResponseSyntax) **   <a name="opensearchservice-CompareDomainConfiguration-response-TargetDomainArn"></a>
The Amazon Resource Name (ARN) of the domain that was compared against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`

## Errors
<a name="API_CompareDomainConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_CompareDomainConfiguration_Examples"></a>

### Example
<a name="API_CompareDomainConfiguration_Example_1"></a>

This example illustrates one usage of CompareDomainConfiguration.

#### Sample Request
<a name="API_CompareDomainConfiguration_Example_1_Request"></a>

```
POST /2021-01-01/opensearch/compareDomainConfiguration HTTP/1.1
Host: es.us-east-1.amazonaws.com
Content-Type: application/json
Content-Length: 195

{"SourceDomainArn": "arn:aws:es:us-east-1:123456789012:domain/my-primary", "TargetDomainArn": "arn:aws:es:us-west-2:123456789012:domain/my-secondary", "Categories": ["templates", "ism_policies"]}
```

#### Sample Response
<a name="API_CompareDomainConfiguration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "SourceDomainArn": "arn:aws:es:us-east-1:123456789012:domain/my-primary",
  "TargetDomainArn": "arn:aws:es:us-west-2:123456789012:domain/my-secondary",
  "Categories": {
    "templates": {
      "Status": "compared",
      "InSync": 3,
      "SourceOnly": 1,
      "TargetOnly": 0,
      "Diverged": 0,
      "Items": {
        "SourceOnly": [
          "logs-template"
        ],
        "TargetOnly": [],
        "Diverged": []
      },
      "Truncated": false
    },
    "ism_policies": {
      "Status": "compared",
      "InSync": 1,
      "SourceOnly": 0,
      "TargetOnly": 0,
      "Diverged": 1,
      "Items": {
        "SourceOnly": [],
        "TargetOnly": [],
        "Diverged": [
          {
            "Name": "hot-warm-delete",
            "Fields": [
              {
                "Path": "policy.states[0].actions[0].rollover.min_size",
                "SourceValue": "\"50gb\"",
                "TargetValue": "\"30gb\""
              }
            ]
          }
        ]
      },
      "Truncated": false
    }
  }
}
```

## See Also
<a name="API_CompareDomainConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CompareDomainConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CompareDomainConfiguration)
