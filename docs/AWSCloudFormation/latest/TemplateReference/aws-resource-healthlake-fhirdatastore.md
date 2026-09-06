---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-healthlake-fhirdatastore.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore
<a name="aws-resource-healthlake-fhirdatastore"></a>

Creates a Data Store that can ingest and export FHIR formatted data.

**Important**
Please note that when a user tries to do an Update operation via CloudFormation, changes to the Data Store name, Type Version, PreloadDataConfig, or SSEConfiguration will delete their existing Data Store for the stack and create a new one. This will lead to potential loss of data.

## Syntax
<a name="aws-resource-healthlake-fhirdatastore-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-healthlake-fhirdatastore-syntax.json"></a>

```
{
  "Type" : "AWS::HealthLake::FHIRDatastore",
  "Properties" : {
      "[DatastoreName](#cfn-healthlake-fhirdatastore-datastorename)" : {{String}},
      "[DatastoreTypeVersion](#cfn-healthlake-fhirdatastore-datastoretypeversion)" : {{String}},
      "[IdentityProviderConfiguration](#cfn-healthlake-fhirdatastore-identityproviderconfiguration)" : {{IdentityProviderConfiguration}},
      "[PreloadDataConfig](#cfn-healthlake-fhirdatastore-preloaddataconfig)" : {{PreloadDataConfig}},
      "[SseConfiguration](#cfn-healthlake-fhirdatastore-sseconfiguration)" : {{SseConfiguration}},
      "[Tags](#cfn-healthlake-fhirdatastore-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-healthlake-fhirdatastore-syntax.yaml"></a>

```
Type: AWS::HealthLake::FHIRDatastore
Properties:
  [DatastoreName](#cfn-healthlake-fhirdatastore-datastorename): {{String}}
  [DatastoreTypeVersion](#cfn-healthlake-fhirdatastore-datastoretypeversion): {{String}}
  [IdentityProviderConfiguration](#cfn-healthlake-fhirdatastore-identityproviderconfiguration): {{
    IdentityProviderConfiguration}}
  [PreloadDataConfig](#cfn-healthlake-fhirdatastore-preloaddataconfig): {{
    PreloadDataConfig}}
  [SseConfiguration](#cfn-healthlake-fhirdatastore-sseconfiguration): {{
    SseConfiguration}}
  [Tags](#cfn-healthlake-fhirdatastore-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-healthlake-fhirdatastore-properties"></a>

`DatastoreName`  <a name="cfn-healthlake-fhirdatastore-datastorename"></a>
The data store name (user-generated).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatastoreTypeVersion`  <a name="cfn-healthlake-fhirdatastore-datastoretypeversion"></a>
The FHIR release version supported by the data store. Current support is for version `R4`.
*Required*: Yes
*Type*: String
*Allowed values*: `R4`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityProviderConfiguration`  <a name="cfn-healthlake-fhirdatastore-identityproviderconfiguration"></a>
The identity provider configuration selected when the data store was created.
*Required*: No
*Type*: [IdentityProviderConfiguration](aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreloadDataConfig`  <a name="cfn-healthlake-fhirdatastore-preloaddataconfig"></a>
The preloaded Synthea data configuration for the data store.
*Required*: No
*Type*: [PreloadDataConfig](aws-properties-healthlake-fhirdatastore-preloaddataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SseConfiguration`  <a name="cfn-healthlake-fhirdatastore-sseconfiguration"></a>
The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store.
*Required*: No
*Type*: [SseConfiguration](aws-properties-healthlake-fhirdatastore-sseconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-healthlake-fhirdatastore-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-healthlake-fhirdatastore-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-healthlake-fhirdatastore-return-values"></a>

### Ref
<a name="aws-resource-healthlake-fhirdatastore-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-healthlake-fhirdatastore-return-values-fn--getatt"></a>

####
<a name="aws-resource-healthlake-fhirdatastore-return-values-fn--getatt-fn--getatt"></a>

`DatastoreArn`  <a name="DatastoreArn-fn::getatt"></a>
The Data Store ARN is generated during the creation of the Data Store and can be found in the output from the initial Data Store creation request.

`DatastoreEndpoint`  <a name="DatastoreEndpoint-fn::getatt"></a>
The endpoint for the created Data Store.

`DatastoreId`  <a name="DatastoreId-fn::getatt"></a>
The Amazon generated Data Store id. This id is in the output from the initial Data Store creation call.

`DatastoreStatus`  <a name="DatastoreStatus-fn::getatt"></a>
The status of the FHIR Data Store. Possible statuses are ‘CREATING’, ‘ACTIVE’, ‘DELETING’, ‘DELETED’.
