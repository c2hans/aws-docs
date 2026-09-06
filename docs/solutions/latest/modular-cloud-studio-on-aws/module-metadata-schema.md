---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/module-metadata-schema.html
---

# Module metadata schema
<a name="module-metadata-schema"></a>

```
$schema: http://json-schema.org/draft-04/schema#
title: Modular Cloud Studio on AWS Module Metadata
description: >-
 Metadata for a Modular Cloud Studio on AWS module.
 The module metadata is included in the metadata section of an AWS CloudFormation template.
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html
 This schema describes how the template metadata must be formatted to describe a module.
 The Module property is required and serves as the root of the Module Metadata.
 Any additional properties are allowed as part of AWS CloudFormation Metadata.

type: object
additionalProperties: true

required:
 - Module

properties:
 Module:
 $ref: '#/definitions/Module'

definitions:
 Module:
 title: Module
 description: Root of Modular Cloud Studio on AWS Module Metadata

 type: object
 additionalProperties: false

 required:
 - MetadataType
 - MetadataVersion
 - Revision

 properties:
 MetadataType:
 description: Indicates that this is Modular Cloud Studio on AWS Metadata
 type: string
 enum:
 - Modular Cloud Studio on AWS
 MetadataVersion:
 title: Metadata version
 description: >-
 Version of this metadata. 2024-01-23 is the only supported version.
 type: string
 enum:
 2024-01-23
 Revision:
 title: Revision identifier
 description: Semantic version that is unique from all other revisions.
 type: string
 Inputs:
 title: Inputs - optional
 description: Parameters this module depends on from other modules.
 type: array
 minItems: 1
 items:
 $ref: '#/definitions/Input'
 Outputs:
 title: Outputs - optional
 description: Parameters this module creates to share with other modules.
 type: array
 minItems: 1
 items:
 $ref: '#/definitions/Output'

 Input:
 title: Input
 description: Required input parameter from SSM parameter store.
 type: object
 additionalProperties: false
 required:
 - Name
 - Type
 properties:
 Name:
 $ref: '#/definitions/ParameterName'
 Type:
 $ref: '#/definitions/ParameterType'
 Remote: $ref: '#/definitions/RemoteParameter
 Description:
 type: string
 minLength: 1
 maxLength: 1024

 Output:
 title: Output
 description: Output parameter this modules creates in SSM parameter store.
 type: object
 additionalProperties: false
 required:
 - Name
 - Type
 properties:
 Name:
 $ref: '#/definitions/ParameterName'
 Type:
 $ref: '#/definitions/ParameterType'
 Description:
 type: string
 minLength: 1
 maxLength: 1024

 ParameterName:
 title: Name
 description: >-
 The name of the parameter this module creates or depends on. Parameters are AWS Systems Manager (SSM) parameters so the names follow the constraints for a SSM parameter name.

 This name is almost a fully qualified name. Each Modular Cloud Studio on AWS deployment generates a unique deployment ID that must be used as the root of the parameter name. This name includes only the part of the fully qualified name that follows the deployment ID. For example, if the fully qualified parameter name is as follows...

 '/mcs-123abc46def/Network/VPC/vpc-id'

 ...this name value should be as follows...

 '/Network/VPC/vpc-id'

 It must begin with a slash character ('/') followed the category, then a slash character ('/'), then the rest of the name.
 type: string
 minLength: 2
 maxLength: 512
 pattern:
'^/(Network|Identity|WorkstationManagement|Storage|PixelStreaming|Core)(/[a-zA-Z0-9_.-]+)\{1,14}$'

 ParameterType:
 title: Type
 description: Data type of the parameter.
 type: string
 maxLength: 128
 enum:
 - 'ssm:string'

 RemoteParameter:
 title: Remote
 description: Set this property to True if a Spoke module has a dependency on a parameter in the Hub region.
 type: boolean
 default: false
```
