---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/drm-session-key-exclusion.html
---

# Excluding DRM session keys in AWS Elemental MediaPackage
<a name="drm-session-key-exclusion"></a>

MediaPackage supports excluding session keys from HLS and LL-HLS multivariant playlists to improve compatibility with legacy clients and provide more granular access control.

## Overview
<a name="drm-session-key-exclusion-overview"></a>

By default, MediaPackage includes `EXT-X-SESSION-KEY` tags in HLS multivariant playlists when DRM is enabled. These tags allow clients to pre-fetch encryption keys, which can improve playback performance. However, some scenarios require excluding these session keys:
+ **Legacy client compatibility** - Some older HLS clients have issues processing session keys and may fail to play content when these tags are present.
+ **Access control** - When using manifest filtering to control access to specific content variants, you may want to provide key information only for the streams a client actually has access to, rather than exposing all keys in the session key tags.

When session keys are excluded, encryption key information is still available in the individual media playlists through `EXT-X-KEY` tags, ensuring that DRM functionality remains intact.

## Configuration options
<a name="drm-session-key-exclusion-configuration"></a>

You can exclude session keys using two methods:
+ **Static configuration** - Configure the setting on the origin endpoint HLS or LL-HLS manifests to exclude session keys. This is done through the **DRM settings** in the filter configuration. For console instructions, see [Manifest fields](endpoints-create.md#endpoints-manifest).
+ **Dynamic exclusion** - Use the `aws.drmsettings=exclude_session_keys` query parameter to exclude session keys on a per-request basis. For more information, see [Manifest filtering](manifest-filtering.md).

**Note**
If session key exclusion is enabled in the static configuration, it cannot be overridden using query parameters. This follows the standard MediaPackage pattern where static filters take precedence over dynamic parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
