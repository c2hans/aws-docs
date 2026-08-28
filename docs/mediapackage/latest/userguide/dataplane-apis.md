---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/dataplane-apis.html
---

# Working with data plane APIs in AWS Elemental MediaPackage
<a name="dataplane-apis"></a>

MediaPackage uses three data plane actions for ingesting and egressing video content. MediaPackage does not use these actions to configure Channel Group, Channel, or Origin Endpoint resources.

## PutObject
<a name="dataplane-apis-putobject"></a>

During ingest, uploads video segments from an encoder into a MediaPackage channel.

To call `PutObject`, perform an HTTP `GET` request to the ingest URL for a channel.

For more information about video format requirements for `PutObject`, see [Supported input types](supported-inputs.md#supported-types-live).

## GetObject
<a name="dataplane-apis-getobject"></a>

Download video segments from an origin endpoint in MediaPackage.

To call `GetObject`, perform an HTTP `GET` request to an egress URL on an origin endpoint.

## GetHeadObject
<a name="dataplane-apis-getheadobject"></a>

Retrieves just the HTTP headers of the video content.

To call `GetHeadObject`, perform an HTTP `HEAD` request to an egress URL on an origin endpoint.

You can dynamically produce client manifests by appending parameters to the playback request. The following topics provide information about the available query parameters:
+ To use query parameters to filter manifests based on audio, subtitle, and video values, see [Manifest filtering from AWS Elemental MediaPackage](manifest-filtering.md).
+ To use query parameters to make live streams available for on-demand viewing for up to 14 days, see [Time-shifted query parameters in AWS Elemental MediaPackage](msettings-params.md).

## HarvestObject
<a name="dataplane-apis-harvestobject"></a>

Uploads the specified manifest or segment directly to a bucket in Amazon S3. For information about harvesting live-to-VOD assets in MediaPackage, see [Creating live-to-VOD assets with MediaPackage](live-to-vod.md).

To call `HarvestObject`, perform an HTTP `POST` request to an egress URL, including the manifest or segment path. In the request headers, include the S3 destination bucket name and key.

**Example**

```
POST {{egress_domain}}/channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}}/{{manifest_or_segment_path}} HTTP/1.1

X-Amz-Source-MediaPackage-S3-Dst-Bucket-Name: {{amzn-s3-demo-bucket/path}}
X-Amz-Source-MediaPackage-S3-Dst-Object-Key: {{amzn-s3-demo-bucket-key}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
