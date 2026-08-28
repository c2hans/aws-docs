---
source_url: https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html
---

# SPEKE API specification
<a name="speke-api-specification"></a>

This is the REST API specification for Secure Packager and Encoder Key Exchange (SPEKE). Use this specification to provide DRM copyright protection for customers who use encryption.

In a video streaming workflow, the encryption engine communicates with the DRM platform key provider to request content keys. These keys are highly sensitive, so it is critical that the key provider and encryption engine establish a highly secure, trusted communication channel. You can also encrypt the content keys in the document for more secure, end-to-end encryption.

This specification addresses the following goals:
+ Define a simple, trusted, highly secure interface that DRM vendors and customers can use to integrate with encryptors when content encryption is required.
+ Cover VOD and live workflows, and include the error conditions and the authentication mechanisms that are required for robust, highly secure communication between encryptors and DRM key provider endpoints.
+ Include support for HLS, MSS, and DASH packaging and their common DRM systems: FairPlay, PlayReady, and Widevine/CENC.
+ Keep the specification simple and extensible, to support future DRM systems.
+ Use a simple REST API.

**Note**
Copyright 2021, Amazon Web Services, Inc. or its affiliates. All rights reserved.
The documentation is made available under the Creative Commons Attribution-ShareAlike 4.0 International License.
THE MATERIAL CONTAINED HEREIN IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS OF THIS MATERIAL BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS MATERIAL OR THE USE OR OTHER DEALINGS OF THIS MATERIAL.

**Topics**
+ [Authentication required for SPEKE](authentication.md)
+ [SPEKE API v1](the-speke-api.md)
+ [SPEKE API v2](the-speke-api-v2.md)
+ [License for the SPEKE API specification](license.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Packager and Encoder Key Exchange API Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query speke` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
