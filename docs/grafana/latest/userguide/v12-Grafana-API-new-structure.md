---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/v12-Grafana-API-new-structure.html
---

# New API structure
<a name="v12-Grafana-API-new-structure"></a>

Starting in Grafana version 12, Grafana HTTP APIs are transitioning to a new standardized API structure with consistent versioning. The new APIs follow a Kubernetes-style path format:

```
/apis/<group>/<version>/namespaces/default/<resource>[/<name>]
```

Where:
+ **group** – Organizes related functionality into logical collections. For example, `playlist.grafana.app` for playlist operations.
+ **version** – Uses semantic versioning with stability levels: `v1alpha1` (experimental), `v1beta1` (pre-release), and `v1` (GA, stable with backward compatibility guarantees).
+ **resource** – The resource type, such as `playlists` or `dashboards`.
+ **name** – The unique identifier for a specific resource instance. Used for Get, Update, and Delete operations.

API responses follow a standardized format with `kind`, `apiVersion`, `metadata`, and `spec` fields.

For more information about the new API structure, see [New API Structure](https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/apis/) in the *Grafana Labs documentation*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
