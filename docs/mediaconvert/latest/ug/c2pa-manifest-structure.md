---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/c2pa-manifest-structure.html
---

# C2PA manifest structure
<a name="c2pa-manifest-structure"></a>

When you embed a C2PA manifest in your MP4 output, MediaConvert generates a manifest with the following components:

**Claim generator information**
Identifies MediaConvert as the service that generated the manifest.

**Format**
Specifies the media format (video/mp4).

**Assertions**
Includes statements about actions performed on the content, such as:
+ `c2pa.opened`: Indicates the content was opened for processing
+ `c2pa.transcoded`: Indicates the content was transcoded

**Asset hash**
A cryptographic hash of the media content to verify its integrity. MediaConvert uses the SHA-256 hashing algorithm for asset validation.

**Digital signature**
A signature created with your KMS key that verifies the authenticity of the manifest. The signature includes a timestamp token from DigiCert's timestamp authority (http://timestamp.digicert.com) to ensure long-term signature validation.

The manifest is embedded in the MP4 file using a standard C2PA UUID box, placed after the FTYP box and before the MOOV box.

**Note**
If your input file already contains C2PA manifests, MediaConvert does not preserve them in the output. Instead, it generates a new manifest.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
