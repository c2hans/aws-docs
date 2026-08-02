---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html
---

# Resource type schema
<a name="resource-type-schema"></a>

To be considered valid, your resource type's schema must adhere to the [Resource provider definition schema](https://github.com/aws-cloudformation/aws-cloudformation-rpdk/blob/master/src/rpdk/core/data/schema/provider.definition.schema.v1.json). This meta-schema provides a means of validating your resource specification during resource development.

## Syntax
<a name="resource-type-schema-syntax"></a>

Below is the structure for a typical resource type schema. For the complete meta-schema definition, see the [Resource Provider Definition Schema](https://github.com/aws-cloudformation/cloudformation-cli/blob/master/src/rpdk/core/data/schema/provider.definition.schema.v1.json) on [GitHub](https://github.com).

```
{
    "typeName": "string",
    "description": "string",
    "sourceUrl": "string",
    "documentationUrl": "string",
    "replacementStrategy": "create_then_delete" | "delete_then_create",
    "taggable": true | false,
    "tagging": {
      "taggable": true | false,
      "tagOnCreate": true | false,
      "tagUpdatable": true | false,
      "cloudFormationSystemTags": true | false,
      "tagProperty": "json-pointer",
    },
    "definitions": {
        "definitionName": {
          . . .
        }
    },
    "properties": {
         "propertyName": {
            "description": "string",
            "type": "string",
             . . .
            },
        },
    },
    "required": [
        "propertyName"
    ],
    "propertyTransform": {
      {
        "/properties/propertyName": "transform"
      }
    },
    "handlers": {
        "create": {
            "permissions": [
                "permission"
            ],
            "timeoutInMinutes": integer
        },
        "read": {
            "permissions": [
                "permission"
            ],
            "timeoutInMinutes": integer
        },
        "update": {
            "permissions": [
                "permission"
            ],
            "timeoutInMinutes": integer
        },
        "delete": {
            "permissions": [
                "permission"
            ],
            "timeoutInMinutes": integer
        },
        "list": {
            "permissions": [
                "permission"
            ],
            "timeoutInMinutes": integer
        }
    },
    "readOnlyProperties": [
        "/properties/propertyName"
    ],
    "writeOnlyProperties": [
        "/properties/propertyName"
    ],
    "conditionalCreateOnlyProperties": [
        "/properties/propertyName"
    ],
    "nonPublicProperties": [
        "/properties/propertyName"
    ],
    "nonPublicDefinitions": [
        "/properties/propertyName"
    ],
    "createOnlyProperties": [
        "/properties/propertyName"
    ],
    "deprecatedProperties": [
        "/properties/propertyName"
    ],
    "primaryIdentifier": [
        "/properties/propertyName"
    ],
    "additionalIdentifiers": [
        [ "/properties/propertyName" ]
    ],
    "typeConfiguration": {
      . . .
    },
    "resourceLink": {
      "templateUri": "string",
      "mappings": "json-pointer"
    },
}
```

## Properties
<a name="resource-type-schema-properties"></a>

Below are the properties for a typical resource type schema.

`typeName`  <a name="schema-properties-typeName"></a>
The unique name for your resource. Specifies a three-part namespace for your resource, with a recommended pattern of `Organization::Service::Resource`.
The following organization namespaces are reserved and can't be used in your resource type names:
+ `Alexa`
+ `AMZN`
+ `Amazon`
+ `ASK`
+ `AWS`
+ `Custom`
+ `Dev`
 *Required*: Yes
 *Pattern*: `^[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}::[a-zA-Z0-9]{2,64}$`

`description`  <a name="schema-properties-description"></a>
A short description of the resource. This will be displayed in the CloudFormation console.
*Required*: Yes

`sourceUrl`  <a name="schema-properties-sourceUrl"></a>
The URL of the source code for this resource, if public.

`documentationUrl`  <a name="schema-properties-documentationurl"></a>
The URL of a page providing detailed documentation for this resource.
While the resource schema itself should include complete and accurate property descriptions, the documentationURL property enables you to provide users with documentation that describes and explains the resource in more detail, including examples, use cases, and other detailed information.

`replacementStrategy`  <a name="schema-properties-replacementstrategy"></a>
The order of replacement when a resource update necessitates replacing the existing resource with a new resource. For example, updating a resource property that is listed in `createonlyProperties` results in a new resource being created to replace the existing resource.
By default, when updating a resource that requires replacement, CloudFormation first creates the new resource, and then delete the old resource. However, some resources can only exist one at a time in a given account/region. For these resources, this attribute can be used to instruct CloudFormation to delete the existing resource before creating its replacement.
For more information on how resources are updated, see [Update behaviors of stack resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html) in the *CloudFormation User Guide*.
*Valid values*: `create_then_delete` \| `delete_then_create`

`taggable`  <a name="schema-properties-taggable"></a>
Deprecated. Use the `tagging` element instead.

`tagging`  <a name="schema-properties-tagging"></a>
Contains properties that specify the resource type's support for tags.
If your resource type does not support tagging, you must set `taggable` to `false` or your resource type will fail contract testing.
`taggable`  <a name="schema-properties-tagging-taggable"></a>
Whether this resource type supports tagging.
If your resource type does not support tagging, you must set `taggable` to `false` or your resource type will fail contract testing.
The default is `true`.
`tagOnCreate`  <a name="schema-properties-tagging-tagoncreate"></a>
Whether this resource type supports tagging resources upon creation.
The default is `true`.
`tagUpdatable`  <a name="schema-properties-tagging-tagupdatable"></a>
Whether this resource type supports updating tags during resource update operations.
The default is `true`.
`cloudFormationSystemTags`  <a name="schema-properties-tagging-cloudformationsystemtags"></a>
Whether this resource type supports CloudFormation system tags.
The default is `true`.
`tagProperty`  <a name="schema-properties-tagging-tagproperty"></a>
A reference to where you have defined the `Tags` property in this resource type schema.
The default is `/properties/Tags`.

`definitions`  <a name="schema-properties-definitions"></a>
Use the `definitions` block to provide shared resource property schemas.
It's considered a best practice is to use the `definitions` section to define schema elements that may be used at multiple points in your resource type schema. You can then use a JSON pointer to reference that element at the appropriate places in your resource type schema.

`properties`  <a name="schema-properties-properties"></a>
The properties of the resource.
All properties of a resource must be expressed in the schema. Arbitrary inputs aren't allowed. A resource must contain at least one property.
Nested properties are not allowed. Instead, define any nested properties in the `definitions` element, and use a `$ref` pointer to reference them in the desired property.
*Required*: Yes
`propertyName`  <a name="schema-properties-propertyname"></a>
`insertionOrder`  <a name="schema-properties-properties-insertionorder"></a>
For properties of type `array`, set to `true` to specify that the order in which array items are specified must be honored, and that changing the order of the array will indicate a change in the property.
The default is `true`.
`dependencies`  <a name="schema-properties-properties-dependencies"></a>
Any properties that are required if this property is specified.
`patternProperties`  <a name="schema-properties-properties-patternproperties"></a>
Use to specify a specification for key-value pairs.

```
"type": "object",
"propertyNames": {
   "format": "regex"
}
```
`properties`  <a name="schema-properties-properties-properties"></a>
*Minimum*: 1
`patternProperties`
*Pattern:* `^[A-Za-z0-9]{1,64}$`
Specifies a pattern that properties must match to be valid.
`allOf`  <a name="schema-properties-properties-allof"></a>
The property must contain all of the data structures define here.
Contains a single schema. A list of schemas is not allowed.
*Minimum*: 1
`anyOf`  <a name="schema-properties-properties-anyof"></a>
The property can contain any number of the data structures define here.
Contains a single schema. A list of schemas is not allowed.
*Minimum*: 1
`oneOf`  <a name="schema-properties-properties-oneof"></a>
The property must contain only one of the data structures define here.
Contains a single schema. A list of schemas is not allowed.
*Minimum*: 1
`items`  <a name="schema-properties-properties-items"></a>
For properties of type array, defines the data structure of each array item.
Contains a single schema. A list of schemas is not allowed.
In addition, the following elements, defined in [draft-07](https://json-schema.org/draft-07) of the [JSON Schema](https://json-schema.org/), are allowed in the `properties` object:
+ $ref
+ $comment
+ title
+ description
+ examples
+ default
+ multipleOf
+ maximum
+ exclusiveMaximum
+ minimum
+ exclusiveMinimum
+ minLength
+ pattern
+ maxItems
+ minItems
+ uniqueItems
+ contains
+ maxProperties
+ required
+ const
+ enum
+ type
+ format

`propertyTransform`  <a name="schema-properties-propertytransform"></a>
One or more transforms to apply to the property value when comparing for drift. For more information, see [Preventing false drift detection results for resource types](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model-false-drift.html).

`remote`  <a name="schema-properties-remote"></a>
Reserved for CloudFormation use.

`readOnlyProperties`  <a name="schema-properties-readonlyproperties"></a>
Resource properties that can be returned by a `read` or `list` request, but can't be set by the user.
*Type*: List of JSON pointers

`writeOnlyProperties`  <a name="schema-properties-writeonlyproperties"></a>
Resource properties that can be specified by the user, but can't be returned by a `read` or `list` request. Write-only properties are often used to contain passwords, secrets, or other sensitive data.
*Type*: List of JSON pointers

`conditionalCreateOnlyProperties`  <a name="schema-properties-conditionalcreateonlyproperties"></a>
A list of JSON pointers for properties that can only be updated under certain conditions. For example, you can upgrade the engine version of an RDS DBInstance but you cannot downgrade it. When updating this property for a resource in a CloudFormation stack, the resource will be replaced if it cannot be updated.
*Type*: List of JSON pointers

`nonPublicProperties`  <a name="schema-properties-nonpublicproperties"></a>
A list of JSON pointers for properties that are hidden. These properties will still be used but will not be visible
*Type*: List of JSON pointers

`nonPublicDefinitions`  <a name="schema-properties-nonpublicdefinitions"></a>
A list of JSON pointers for definitions that are hidden. These definitions will still be used but will not be visible
*Type*: List of JSON pointers

`createOnlyProperties`  <a name="schema-properties-createonlyproperties"></a>
Resource properties that can be specified by the user only during resource creation.
Any property not explicitly listed in the `createOnlyProperties` element can be specified by the user during a resource update operation.
*Type*: List of JSON pointers

`deprecatedProperties`  <a name="schema-properties-deprecatedproperties"></a>
Resource properties that have been deprecated by the underlying service provider. These properties are still accepted in create and update operations. However they may be ignored, or converted to a consistent model on application. Deprecated properties are not guaranteed to be returned by read operations.
*Type*: List of JSON pointers

`primaryIdentifier`  <a name="schema-properties-primaryidentifier"></a>
The uniquely identifier for an instance of this resource type. An identifier is a non-zero-length list of JSON pointers to properties that form a single key. An identifier can be a single or multiple properties to support composite-key identifiers.
*Type*: List of JSON pointers
*Required*: Yes

`additionalIdentifiers`  <a name="schema-properties-additionalidentifiers"></a>
An optional list of lists of supplementary identifiers, each of which uniquely identifies an instance of this resource type. An identifier can be a single property, or multiple properties to construct composite-key identifiers.
*Type*: List of lists
*Minimum*: 1

`handlers`  <a name="schema-properties-handlers"></a>
Specifies the provisioning operations which can be performed on this resource type. The handlers specified determine what provisioning actions CloudFormation takes with respect to the resource during various stack operations.
+ If the resource type doesn't contain `create`, `read`, and `delete` handlers, CloudFormation can't actually provision the resource.
+ If the resource type doesn't contain an `update` handler, CloudFormation can't update the resource during stack update operations, and will instead replace it.
If your resource type calls AWS APIs in any of its handlers, you must create an *[IAM execution role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)* that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. For more information, see [Accessing AWS APIs from a Resource Type](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-develop.html#resource-type-develop-executionrole).
`create`  <a name="schema-properties-handlers-create"></a>
permissions  <a name="schema-properties-handlers-create-permissions"></a>
A string array that specifies the AWS permissions needed to invoke the create handler.
You must specify at least one permission for each handler.
*Required*: Yes
timeoutInMinutes  <a name="schema-properties-handlers-create-timeoutinminutes"></a>
An integer specifying the timeout for the entire operation to be interpreted by the invoker of the handler, in minutes.
*Minimum*: 2
*Maximum*: 2160
*Default*: 120
*Required*: No
`read`  <a name="schema-properties-handlers-read"></a>
`permissions`  <a name="schema-properties-handlers-read-permissions"></a>
A string array that specifies the AWS permissions needed to invoke the read handler.
You must specify at least one permission for each handler.
*Required*: Yes
timeoutInMinutes  <a name="schema-properties-handlers-read-timeoutinminutes"></a>
An integer specifying the timeout for the entire operation to be interpreted by the invoker of the handler, in minutes.
*Minimum*: 2
*Maximum*: 2160
*Default*: 120
*Required*: No
`update`  <a name="schema-properties-handlers-update"></a>
permissions  <a name="schema-properties-handlers-update-permissions"></a>
A string array that specifies the AWS permissions needed to invoke the update handler.
You must specify at least one permission for each handler.
*Required*: Yes
timeoutInMinutes  <a name="schema-properties-handlers-update-timeoutinminutes"></a>
An integer specifying the timeout for the entire operation to be interpreted by the invoker of the handler, in minutes.
*Minimum*: 2
*Maximum*: 2160
*Default*: 120
*Required*: No
`delete`  <a name="schema-properties-handlers-delete"></a>
permissions  <a name="schema-properties-handlers-delete-permissions"></a>
A string array that specifies the AWS permissions needed to invoke the delete handler.
You must specify at least one permission for each handler.
*Required*: Yes
timeoutInMinutes  <a name="schema-properties-handlers-delete-timeoutinminutes"></a>
An integer specifying the timeout for the entire operation to be interpreted by the invoker of the handler, in minutes.
*Minimum*: 2
*Maximum*: 2160
*Default*: 120
*Required*: No
`list`  <a name="schema-properties-handlers-list"></a>
The `list` handler must at least return the resource's primary identifier.
permissions  <a name="schema-properties-handlers-list-permissions"></a>
A string array that specifies the AWS permissions needed to invoke the list handler.
You must specify at least one permission for each handler.
*Required*: Yes
timeoutInMinutes  <a name="schema-properties-handlers-list-timeoutinminutes"></a>
An integer specifying the timeout for the entire operation to be interpreted by the invoker of the handler, in minutes.
*Minimum*: 2
*Maximum*: 2160
*Default*: 120
*Required*: No

`allOf`  <a name="schema-properties-allof"></a>
The resource must contain all of the data structures defined here.
*Minimum*: 1

`anyOf`  <a name="schema-properties-anyof"></a>
The resource can contain any number of the data structures define here.
*Minimum*: 1

`oneOf`  <a name="schema-properties-oneof"></a>
The resource must contain only one of the data structures define here.
*Minimum*: 1

`resourceLink`  <a name="schema-properties-resourcelink"></a>
A template-able link to a resource instance. External service links must be absolute, HTTPS URIs.
templateUri  <a name="schema-properties-resourcelink-templateuri"></a>
*Required*: Yes
*Pattern*: `^(/|https:)`
mappings  <a name="schema-properties-resourcelink-mappings"></a>
*Required*: Yes
*Type*: List of JSON pointers

`typeConfiguration`  <a name="schema-properties-typeconfiguration"></a>
A type configuration schema that defines any properties that the user must specify for all instances of the extension in a given account and Region. For example, if your extension needs to access a third-party web service, you can include a configuration schema for the user to specify their credentials for that service.
Your configuration definition must validate against the [provider configuration definition meta-schema](https://github.com/aws-cloudformation/cloudformation-cli/blob/master/src/rpdk/core/data/schema/provider.configuration.definition.schema.v1.json).
When the user specifices a resource, they can sets the configuration. CloudFormation validates it against the configuration definition, and then saves this information at the Region level. From then on, CloudFormation can access that configuration schema during operations involving any instances of that extension in the Region. Configurations are available to CloudFormation during all resource operations, including `read` and `list` events that don't explicitly involve a stack template.
The `CloudFormation` property name is reserved, and cannot be used to define any properties in your configuration definition.
For more information, see [Defining the account-level configuration of an extension](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration).
