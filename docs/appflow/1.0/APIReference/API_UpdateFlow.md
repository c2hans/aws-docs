---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpdateFlow.html
---

# UpdateFlow
<a name="API_UpdateFlow"></a>

 Updates an existing flow.

## Request Syntax
<a name="API_UpdateFlow_RequestSyntax"></a>

```
POST /update-flow HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "destinationFlowConfigList": [
      {
         "apiVersion": "{{string}}",
         "connectorProfileName": "{{string}}",
         "connectorType": "{{string}}",
         "destinationConnectorProperties": {
            "CustomConnector": {
               "customProperties": {
                  "{{string}}" : "{{string}}"
               },
               "entityName": "{{string}}",
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "idFieldNames": [ "{{string}}" ],
               "writeOperationType": "{{string}}"
            },
            "CustomerProfiles": {
               "domainName": "{{string}}",
               "objectTypeName": "{{string}}"
            },
            "EventBridge": {
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "object": "{{string}}"
            },
            "Honeycode": {
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "object": "{{string}}"
            },
            "LookoutMetrics": {
            },
            "Marketo": {
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "object": "{{string}}"
            },
            "Redshift": {
               "bucketPrefix": "{{string}}",
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "intermediateBucketName": "{{string}}",
               "object": "{{string}}"
            },
            "S3": {
               "bucketName": "{{string}}",
               "bucketPrefix": "{{string}}",
               "s3OutputFormatConfig": {
                  "aggregationConfig": {
                     "aggregationType": "{{string}}",
                     "targetFileSize": {{number}}
                  },
                  "fileType": "{{string}}",
                  "prefixConfig": {
                     "pathPrefixHierarchy": [ "{{string}}" ],
                     "prefixFormat": "{{string}}",
                     "prefixType": "{{string}}"
                  },
                  "preserveSourceDataTyping": {{boolean}}
               }
            },
            "Salesforce": {
               "dataTransferApi": "{{string}}",
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "idFieldNames": [ "{{string}}" ],
               "object": "{{string}}",
               "writeOperationType": "{{string}}"
            },
            "SAPOData": {
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "idFieldNames": [ "{{string}}" ],
               "objectPath": "{{string}}",
               "successResponseHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}"
               },
               "writeOperationType": "{{string}}"
            },
            "Snowflake": {
               "bucketPrefix": "{{string}}",
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "intermediateBucketName": "{{string}}",
               "object": "{{string}}"
            },
            "Upsolver": {
               "bucketName": "{{string}}",
               "bucketPrefix": "{{string}}",
               "s3OutputFormatConfig": {
                  "aggregationConfig": {
                     "aggregationType": "{{string}}",
                     "targetFileSize": {{number}}
                  },
                  "fileType": "{{string}}",
                  "prefixConfig": {
                     "pathPrefixHierarchy": [ "{{string}}" ],
                     "prefixFormat": "{{string}}",
                     "prefixType": "{{string}}"
                  }
               }
            },
            "Zendesk": {
               "errorHandlingConfig": {
                  "bucketName": "{{string}}",
                  "bucketPrefix": "{{string}}",
                  "failOnFirstDestinationError": {{boolean}}
               },
               "idFieldNames": [ "{{string}}" ],
               "object": "{{string}}",
               "writeOperationType": "{{string}}"
            }
         }
      }
   ],
   "flowName": "{{string}}",
   "metadataCatalogConfig": {
      "glueDataCatalog": {
         "databaseName": "{{string}}",
         "roleArn": "{{string}}",
         "tablePrefix": "{{string}}"
      }
   },
   "sourceFlowConfig": {
      "apiVersion": "{{string}}",
      "connectorProfileName": "{{string}}",
      "connectorType": "{{string}}",
      "incrementalPullConfig": {
         "datetimeTypeFieldName": "{{string}}"
      },
      "sourceConnectorProperties": {
         "Amplitude": {
            "object": "{{string}}"
         },
         "CustomConnector": {
            "customProperties": {
               "{{string}}" : "{{string}}"
            },
            "dataTransferApi": {
               "Name": "{{string}}",
               "Type": "{{string}}"
            },
            "entityName": "{{string}}"
         },
         "Datadog": {
            "object": "{{string}}"
         },
         "Dynatrace": {
            "object": "{{string}}"
         },
         "GoogleAnalytics": {
            "object": "{{string}}"
         },
         "InforNexus": {
            "object": "{{string}}"
         },
         "Marketo": {
            "object": "{{string}}"
         },
         "Pardot": {
            "object": "{{string}}"
         },
         "S3": {
            "bucketName": "{{string}}",
            "bucketPrefix": "{{string}}",
            "s3InputFormatConfig": {
               "s3InputFileType": "{{string}}"
            }
         },
         "Salesforce": {
            "dataTransferApi": "{{string}}",
            "enableDynamicFieldUpdate": {{boolean}},
            "includeDeletedRecords": {{boolean}},
            "object": "{{string}}"
         },
         "SAPOData": {
            "objectPath": "{{string}}",
            "paginationConfig": {
               "maxPageSize": {{number}}
            },
            "parallelismConfig": {
               "maxParallelism": {{number}}
            }
         },
         "ServiceNow": {
            "object": "{{string}}"
         },
         "Singular": {
            "object": "{{string}}"
         },
         "Slack": {
            "object": "{{string}}"
         },
         "Trendmicro": {
            "object": "{{string}}"
         },
         "Veeva": {
            "documentType": "{{string}}",
            "includeAllVersions": {{boolean}},
            "includeRenditions": {{boolean}},
            "includeSourceFiles": {{boolean}},
            "object": "{{string}}"
         },
         "Zendesk": {
            "object": "{{string}}"
         }
      }
   },
   "tasks": [
      {
         "connectorOperator": {
            "Amplitude": "{{string}}",
            "CustomConnector": "{{string}}",
            "Datadog": "{{string}}",
            "Dynatrace": "{{string}}",
            "GoogleAnalytics": "{{string}}",
            "InforNexus": "{{string}}",
            "Marketo": "{{string}}",
            "Pardot": "{{string}}",
            "S3": "{{string}}",
            "Salesforce": "{{string}}",
            "SAPOData": "{{string}}",
            "ServiceNow": "{{string}}",
            "Singular": "{{string}}",
            "Slack": "{{string}}",
            "Trendmicro": "{{string}}",
            "Veeva": "{{string}}",
            "Zendesk": "{{string}}"
         },
         "destinationField": "{{string}}",
         "sourceFields": [ "{{string}}" ],
         "taskProperties": {
            "{{string}}" : "{{string}}"
         },
         "taskType": "{{string}}"
      }
   ],
   "triggerConfig": {
      "triggerProperties": {
         "Scheduled": {
            "dataPullMode": "{{string}}",
            "firstExecutionFrom": {{number}},
            "flowErrorDeactivationThreshold": {{number}},
            "scheduleEndTime": {{number}},
            "scheduleExpression": "{{string}}",
            "scheduleOffset": {{number}},
            "scheduleStartTime": {{number}},
            "timezone": "{{string}}"
         }
      },
      "triggerType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-clientToken"></a>
The `clientToken` parameter is an idempotency token. It ensures that your `UpdateFlow` request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.
If you omit a `clientToken` value, the AWS SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.
If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken`, Amazon AppFlow considers it a new call to `UpdateFlow`. The token is active for 8 hours.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ -~]+`
Required: No

 ** [description](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-description"></a>
 A description of the flow.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\w!@#\-.?,\s]*`
Required: No

 ** [destinationFlowConfigList](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-destinationFlowConfigList"></a>
 The configuration that controls how Amazon AppFlow transfers data to the destination connector.
Type: Array of [DestinationFlowConfig](API_DestinationFlowConfig.md) objects
Required: Yes

 ** [flowName](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-flowName"></a>
 The specified name of the flow. Spaces are not allowed. Use underscores (\_) or hyphens (-) only.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: Yes

 ** [metadataCatalogConfig](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-metadataCatalogConfig"></a>
Specifies the configuration that Amazon AppFlow uses when it catalogs the data that's transferred by the associated flow. When Amazon AppFlow catalogs the data from a flow, it stores metadata in a data catalog.
Type: [MetadataCatalogConfig](API_MetadataCatalogConfig.md) object
Required: No

 ** [sourceFlowConfig](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-sourceFlowConfig"></a>
 Contains information about the configuration of the source connector used in the flow.
Type: [SourceFlowConfig](API_SourceFlowConfig.md) object
Required: Yes

 ** [tasks](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-tasks"></a>
 A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.
Type: Array of [Task](API_Task.md) objects
Required: Yes

 ** [triggerConfig](#API_UpdateFlow_RequestSyntax) **   <a name="appflow-UpdateFlow-request-triggerConfig"></a>
 The trigger settings that determine how and when the flow runs.
Type: [TriggerConfig](API_TriggerConfig.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowStatus": "string"
}
```

## Response Elements
<a name="API_UpdateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowStatus](#API_UpdateFlow_ResponseSyntax) **   <a name="appflow-UpdateFlow-response-flowStatus"></a>
Indicates the current status of the flow.
Type: String
Valid Values: `Active | Deprecated | Deleted | Draft | Errored | Suspended`

## Errors
<a name="API_UpdateFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
AppFlow/Requester has invalid or missing permissions.
HTTP Status Code: 403

 ** ConflictException **
 There was a conflict when processing the request (for example, a flow with the given name already exists within the account. Check for conflicting resource names and try again.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
 The request would cause a service quota (such as the number of flows) to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_UpdateFlow_Examples"></a>

### Salesforce
<a name="API_UpdateFlow_Example_1"></a>

This example shows a sample request for the `UpdateFlow` API using Salesforce.

#### Sample Request
<a name="API_UpdateFlow_Example_1_Request"></a>

```
{
  "flowName": "testFlow-newpayload",
  "description": "TestFlow",
  "triggerConfig": {
    "triggerType": "OnDemand"
  },
  "sourceFlowConfig": {
    "connectorType": "Salesforce",
    "connectorProfileName": "Connector_Profile_Name",
    "sourceConnectorProperties": {
      "salesforce": {
        "object": "account"
      }
    }
  },
  "destinationFlowConfigList": [
    {
      "connectorType": "S3",
      "connectorProfileName": "Test",
      "destinationConnectorProperties": {
        "s3": {
          "bucketName": "Bucket_Name_value",
          "bucketKey": "Bucket_Name_value"
        }
      }
    }
  ],
  "tasks": [
    {
      "sourceFields": ["CreatedDate"],
      "taskProperties": {},
      "destinationField": "CreatedDate",
      "taskType": "Map"
    },
    {
      "destinationField": "LastActivityDate",
      "sourceFields": ["LastActivityDate"],
      "taskProperties": {},
      "taskType": "Map"
    }
  ]
}
```

### Zendesk
<a name="API_UpdateFlow_Example_2"></a>

This example shows a sample request for the `UpdateFlow` API using Zendesk.

#### Sample Request
<a name="API_UpdateFlow_Example_2_Request"></a>

```
{
  "useDefaultEncryption": false,
  "flowName": "testFlowZendesk",
  "description": "TestFlow",
  "triggerConfig": {
    "triggerType": "OnDemand"
  },
  "sourceFlowConfig": {
    "connectorType": "Zendesk",
    "connectorProfileName": "connector-profile-name",
    "sourceConnectorProperties": {
      "zendesk": {
        "object": "tickets"
      }
    }
  },
  "destinationFlowConfigList": [
    {
      "connectorType": "S3",
      "connectorProfileName": "Test",
      "destinationConnectorProperties": {
        "s3": {
          "bucketName": "Bucket_Name_Value",
          "bucketKey": "Bucket_Name_Value"
        }
      }
    }
  ],
  "tasks": [
    {
      "destinationField": "url",
      "sourceFields": ["url"],
      "taskProperties": {
        "SOURCE_DATA_TYPE": "integer"
      },
      "taskType": "Map"
    }
  ]
}
```

### Google Analytics
<a name="API_UpdateFlow_Example_3"></a>

This example shows a sample request for the `UpdateFlow` API using Google Analytics.

#### Sample Request
<a name="API_UpdateFlow_Example_3_Request"></a>

```
{
  "useDefaultEncryption": false,
  "flowName": "testFlowGAnalytics",
  "description": "TestFlow",
  "triggerConfig": {
    "triggerType": "OnDemand"
  },
  "sourceFlowConfig": {
    "connectorType": "Googleanalytics",
    "connectorProfileName": "connector-profile-name",
    "sourceConnectorProperties": {
      "googleanalytics": {
        "object": "Object_ID"
      }
    }
  },
  "destinationFlowConfigList": [
    {
      "connectorType": "S3",
      "connectorProfileName": "Test",
      "destinationConnectorProperties": {
        "s3": {
          "bucketName": "Bucket_Name_Value",
          "bucketKey": "Bucket_Name_Value"
        }
      }
    }
  ],
  "tasks": [
    {
      "destinationField": "url",
      "sourceFields": ["url"],
      "taskProperties": {
        "SOURCE_DATA_TYPE": "integer"
      },
      "taskType": "Map"
    }
  ]
}
```

### Marketo
<a name="API_UpdateFlow_Example_4"></a>

This example shows a sample request for the `UpdateFlow` API using Marketo.

#### Sample Request
<a name="API_UpdateFlow_Example_4_Request"></a>

```
{
  "flowName": "testMarketo",
  "description": "TestFlow",
  "triggerConfig": {
    "triggerType": "OnDemand"
  },
  "sourceFlowConfig": {
    "connectorType": "Marketo",
    "connectorProfileName": "Connector-profile-new",
    "sourceConnectorProperties": {
      "marketo": {
         "object": "leads"
      }
    }
  },
  "destinationFlowConfigList": [
    {
      "connectorType": "S3",
      "connectorProfileName": "Test",
      "destinationConnectorProperties": {
        "s3": {
          "bucketName": "Bucket_Name_Value",
          "bucketKey": "Bucket_Name_Value"
        }
      }
    }
  ],
  "tasks": [
      {
      "connectorOperator": {
          "marketo":"BETWEEN"
      },
      "sourceFields": [
        "updatedAt"
      ],
      "taskProperties": {
        "DATA_TYPE": "datetime",
        "LOWER_BOUND": "Lower_Bound_value",
        "UPPER_BOUND": "Upper_Bound_value"
      },
      "taskType": "Filter"
    },
    {
      "destinationField": "company",
      "sourceFields": [
        "company"
      ],
      "taskProperties": {
          "SOURCE_DATA_TYPE": "string"
      },
      "taskType": "Map"
    }
  ]
}
```

## See Also
<a name="API_UpdateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/UpdateFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/UpdateFlow)
