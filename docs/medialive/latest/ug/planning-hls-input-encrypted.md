---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/planning-hls-input-encrypted.html
---

# Handling encrypted source content in an HLS source
<a name="planning-hls-input-encrypted"></a>

MediaLive can ingest an HLS source that is encrypted according to the HTTP Live Streaming specification.

**Supported encryption format**

MediaLive supports the following format for encrypted HLS sources:
+ The source content is encrypted with AES-128. MediaLive doesn't support AES-SAMPLE.
+ The source content is encrypted using either static or rotating keys.
+ The manifest includes the `#EXT-X-KEY `tag with these attributes:
  + The `METHOD` attribute specifies AES-128.
  + The URI specifies the license server for the encryption key.
  + The IV is blank or specifies the initialization vector (IV) to use. If the IV is blank, MediaLive uses the value in the `#EXT-X-MEDIA-SEQUENCE` tag as the IV.
+ If both the upstream system and the license server require authentication credentials (user name and password), make sure that the same credentials are used on both servers. MediaLive does not support having different credentials for these two servers.

** How decryption works**

The content owner sets up the main manifest to include the `#EXT-X-KEY` with the method (AES-128), the URL to the license server, and the initialization vector (IV). The content owner places the encryption keys on the license server. When the MediaLive channel that uses this source starts, MediaLive obtains the main manifest and reads the `#EXT-X-KEY `tag for the URL of the license server.

MediaLive connects to the license server and obtains the encryption key. MediaLive starts pulling the content from the upstream system, and decrypts the content using the encryption key and the IV.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
