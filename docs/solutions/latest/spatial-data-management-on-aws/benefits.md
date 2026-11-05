---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/benefits.html
---

# Benefits
<a name="benefits"></a>

The solution addresses these challenges by providing:

## Centralized Data Management
<a name="centralized-data-management"></a>

Manage each dataset as an asset with versions, metadata, and permissions, rather than as loose files in a bucket. Files are stored in Amazon Simple Storage Service (Amazon S3) by content, so identical files are stored once across versions and assets. Use the web portal, desktop client, or APIs to upload, download, and manage files and folders, preserving the data structure.

## Versions and Lineage
<a name="versions-and-lineage"></a>

Every change to an asset creates a new version. Metadata and derived content, such as previews, converted formats, and model outputs, are recorded on the version they describe, so a result stays with the data it was made from, even after later uploads. Assets that a connector creates from another asset record where they came from, so you can trace a result back to its source.

## Automated Metadata Enrichment
<a name="automated-metadata-enrichment"></a>

Streamline the process of adding metadata to your spatial assets at scale. Automatically extract and apply relevant metadata tags, while providing users the ability to review, edit, and bulk-apply custom metadata using predefined templates. You can use file types of your choice. The solution provides enhanced support for metadata enrichment and previews for the following file types, but is designed to extend to new use cases: E57, LAZ, TIFF, GeoTIFF, JPEG, PNG, PLY, GLB, glTF, PDF, and TXT.

## Intelligent Data Discovery
<a name="intelligent-data-discovery"></a>

Organize and access your spatial data using a flexible resource model that supports grouping and access control. Quickly search for assets and files based on system-defined or custom attributes, including geolocation tags. Leverage the map-based dashboard to visually locate and discover assets based on their physical geographic coordinates.

## Seamless Data Interoperability
<a name="seamless-data-interoperability"></a>

Connect your assets to applications, APIs, processing jobs, and machine learning models with connectors. A connector is configuration, so nothing is built or deployed to add an integration. When an asset changes, the connectors approved for its asset template run, and their results return to the asset as metadata, derived files, and new assets. Each run is recorded, so you can see what ran, on which version, and what it produced.

## Governed Integration
<a name="governed-integration"></a>

Administrators approve each connector on the asset templates it can act on, so a connector never touches assets outside that scope. Connectors use roles you control in your own accounts, and their changes are subject to the same permissions and version history as any other change.
