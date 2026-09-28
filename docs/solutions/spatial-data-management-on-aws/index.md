---
source_url: https://docs.aws.amazon.com//solutions/spatial-data-management-on-aws//index.html
---

---
title: 'Spatial Data Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/spatial-data-management-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Spatial Data Management on AWS

Make it easy to store, enrich, and connect your spatial and geospatial data

- **Version**: 1.6.2
- **Released**: 09/2026
- **Author**: AWS
- **Est. deployment time**: 40 mins
- **Estimated cost**: [See details](/solutions/latest/spatial-data-management-on-aws/cost.html)

## Overview

Managing spatial data at scale presents significant challenges for storage, compute, and security requirements. With costly data acquisition and creation, organizations need robust processes to track, integrate, and use spatial assets across spatial workflows. Spatial Data Management on AWS provides a comprehensive solution to store, manage, and connect your spatial data as a single source of truth. You can deploy the solution in your AWS account and use the pre-built client to start uploading and managing your spatial data immediately.

## Benefits

### Centralized data management

Store all your spatial data in a single, secure, scalable and highly available location powered by Amazon S3. You can use the desktop client, CLI or APIs to upload, download, and manage files and folders while preserving the data structure.

### Automated metadata enrichment

Streamline the process of adding metadata to your spatial assets at scale. The solution automatically extracts and applies relevant metadata tags. You can review, edit, and bulk-apply custom metadata using predefined templates.

### Intelligent data discovery

Organize and access your spatial data using a flexible resource model that supports grouping and access control. You can quickly search for assets and files based on system-defined or custom attributes, including geolocation tags. Use the map-based dashboard to visually locate and discover assets based on their physical geographic coordinates.

### Seamless data interoperability

Define connectors to integrate your spatial data stored in S3 with various applications, APIs, and data processing jobs. You can trigger actions and workflows based on events associated with your spatial assets, ensuring seamless data exchange across your pipeline.

## How it works

Deploy Spatial Data Management on AWS through AWS CloudFormation with Amazon S3 for storage. The solution integrates with AWS Deadline Cloud to extract metadata, transform files, and generate previews. Access your assets through web and desktop portals or integrate with your digital twin applications using connectors that you configure directly in the UI. [Open implementation guide](/solutions/latest/spatial-data-management-on-aws/solution-overview.html)

![Architecture diagram](/images/solutions/spatial-data-management-on-aws/images/spatial-data-management.png)

## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/spatial-data-management-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?&templateURL=https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/SpatialDataManagementStack.template&redirectId=SolutionsHub)

## Deployment options

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://solutions-reference.s3.amazonaws.com/spatial-data-management/latest/SpatialDataManagementStack.template)

- **Implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[View guide](/solutions/latest/spatial-data-management-on-aws/solution-overview.html)

- **Client setup**: Windows, macOS, Linux

[Learn more](/solutions/latest/spatial-data-management-on-aws/client-setup.html)

## AWS partner integrations

- **VNTANA Intelligent 3D Model Operation Engine**: Use Spatial Data Management on AWS's connector framework to automate workflows with VNTANA's Intelligent Optimization Engine Container to compress 3D files from over 30 CAD and 3D formats into web, game engine, and VR/AR ready assets.

[Learn more](https://aws.amazon.com/marketplace/pp/prodview-ooio3bidshgy4)

- **Esri ArcGIS Pro Plugin**: Plugin for viewing Spatial Data Management structure in Esri ArcGIS Enterprise, developed by AWS and Esri engineers.

[Learn more](https://github.com/Esri/arcgispro-connector-for-sdma)

- **VEERUM Digital Twin**: Reference connector in Spatial Data Management on AWS processes data for VEERUM's Digital Twin application, enabling remote site access and modification.

[Learn more](https://aws.amazon.com/marketplace/pp/prodview-2y6tkneoovyc2)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/spatial-data-management-on-aws/contact-aws-support.html)
