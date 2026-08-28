---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/window-seconds.html
---

# Limit manifest duration from AWS Elemental MediaPackage
<a name="window-seconds"></a>

To dynamically request shorter manifests than the manifest window that's configured on the endpoint, use the `?aws.manifestsettings=manifest_window_seconds:` query parameter. When used at session initialization, the resulting manifest will conform to the number of seconds that you specify in the parameter. With `manifest_window_seconds`, you can serve manifests that are a variety of lengths, all from the same endpoint.

If `aws.manifestsettings=manifest_window_seconds:` isn't included in the request query parameters, MediaPackage serves a manifest the length of the window that's configured through **Manifest window (sec)** in the manifest settings when the endpoint was created.

Query parameters in the `aws.manifestsettings` namespace provide additional session-level time manipulation options. See [Time-shifted query parameters](msettings-params.md) for an overview.

To filter session-level manifests by audio, video, and subtitle formats, see [Manifest filtering](manifest-filtering.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
