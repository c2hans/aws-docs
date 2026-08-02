---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/module-manifest-schema.html
---

# Module manifest schema
<a name="module-manifest-schema"></a>

```
$schema: http://json-schema.org/draft-04/schema#
title: Modular Cloud Studio on AWS Module Manifest
description: >-
 A Module Manifest describes a module that can be registered with Modular Cloud
 Studio on AWS.
 It lists all available revisions of the module describing where to find them.

type: object
additionalProperties: false

required:
 - $manifest
 - $manifestVersion
 - Name
 - Description
 - Owner
 - Category
 - Revisions

properties:
 $manifest:
 title: Manifest
 description: Indicates that this is a Modular Cloud Studio on AWS Manifest
 type: string
 enum:
 - Modular Cloud Studio on AWS
 $manifestVersion:
 title: Manifest version
 description: Version of this manifest. 2024-01-23 is the only supported version.
 type: string
 enum:
 2024-01-23
 Name:
 title: Module name
 description: An easily identifiable name for the module.
 type: string
 maxLength: 8191
pattern: '^[a-zA-Z0-9]+(?:\s[a-zA-Z0-9]+)*$'
 Description:
 title: Module description
 description: >-
 A description of the module that helps consumers understand what it does.
 type: string
 maxLength: 8191
 Owner:
 title: Owner
 description: The person or organization that publishes this module.
 type: string
 maxLength: 8191
 Category:
 title: Module category
 description: |-
 One of the supported module categories:

 * Network
 * Identity
 * WorkstationManagement
 * Storage
 * PixelStreaming
 * Custom
 type: string
 enum:
 - Network
 - Identity
 - WorkstationManagement
 - Storage
 - PixelStreaming
 - Custom
 SupportDescription:
 title: Support description - optional
 description: >-
 The description of how users should use the email contact and support link.
 type: string
 maxLength: 8191
 SupportEmail:
 title: Support email - optional
 description: The email address to report issues with the module.
 type: string
 maxLength: 254
 SupportUrl:
 title: Support URL - optional
 description: >-
 The URL to a site where users can find support information or file tickets.
 type: string
 pattern: '^https?://'
 maxLength: 2083
 Revisions:
 title: Module revisions
 description: List of all available module revisions.
 type: array
 minItems: 1
 uniqueItems: true
 items:
 $ref: '#/definitions/ModuleRevision'

definitions:
 ModuleRevision:
 description: >-
 Details about where to find a specific revision of the module.

 type: object
 additionalProperties: false

 required:
 - Revision
 - SupportedRegions
 - Compatibility

minProperties: 4
maxProperties: 4
additionalProperties: false

 properties:
 Revision:
 title: Revision identifier
 description: Semantic version that is unique from all other revisions. Check https://regex101.com/r/vkijKf/1/ for more information
 type: string
 pattern: '^(0|[1-9]\\d*)(\\.(0|[1-9]\\d*)){1,2}$'
 TemplateUrl:
 title: Template URL
 description: |-
 The URL of the AWS CloudFormation template in Amazon S3.
 pattern: '^https://'
 maxLength: 2083
 TemplateUrls:
 title: Template URLs
 description: >-
 The URLs of the AWS CloudFormation templates for hub and spoke modules in Amazon S3. The Spoke property is optional and not used for hub-only modules.
 type: object
 required:
 - Hub
 properties:
 Hub:
 title: Hub Template URL
 description: >-
 The URL of the AWS CloudFormation template for the hub module in Amazon S3.
 type: string
 pattern: ^https://
 maxLength: 2083
 Spoke:
 title: Spoke Template URL
 description: >-
 The URL of the AWS CloudFormation template for the spoke module in Amazon S3.
 type: string
 pattern: ^https://
 maxLength: 2083
 SupportedRegions:
 title: Supported regions
 description: >-
 A module may depend on AWS services that are not available in all AWS
 regions. A module must explicitly specify which AWS regions are supported.
 type: array
 minItems: 1
 uniqueItems: true
 items:
 type: string
 Compatibility:
 $ref: '#/definitions/Compatibility'

 Compatibility:
 title: Compatibility
 description: >-
 If a revision is compatible with specific versions of Modular Cloud Studio
 on AWS, it can optionally include a compatibility specification.
 type: object
 additionalProperties: false
 required:
 - MinimumMcsVersion
 - MaximumMcsVersion
 properties:
 MinimumMcsVersion:
 title: Minimum Modular Cloud Studio on AWS version
 description: >-
 Semantic Versioning identifier of the earliest version of Modular Cloud
 Studio on AWS that this revision of the module is compatible with.
 type: string
 minLength: 1
 pattern: '^(0|[1-9]\d*)(\.(0|[1-9]\d*)){1,2}$'
 MaximumMcsVersion:
 title: Maximum Modular Cloud Studio on AWS version
 description: >-
 Semantic Versioning identifier of the latest version of Modular Cloud
 Studio on AWS that this revision of the module is compatible with.
 type: string
 minLength: 1
 pattern: '^(0|[1-9]\d*)(\.(0|[1-9]\d*)){1,2}$'
```
