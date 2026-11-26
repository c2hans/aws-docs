---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability-dashboards-sharing.html
---

# Sharing dashboards

You can share dashboards with other users in your organization through URLs, snapshots, and exports.

## Share through URL
<a name="observability-dashboards-sharing-url"></a>

Copy the dashboard URL from your browser address bar and share it directly. The URL preserves the current time range and filters. You can include dashboard links in bookmarks, runbooks, or incident response documentation.

## Snapshots
<a name="observability-dashboards-sharing-snapshots"></a>

A snapshot captures the current state of a dashboard, including all panel data, at a specific point in time. Snapshots are read-only and do not update when the underlying data changes. Use snapshots to preserve a record of dashboard state during incidents or reviews.

## Import and export definitions
<a name="observability-dashboards-sharing-import-export"></a>

You can export a dashboard definition as JSON and import it into another workspace or environment. This approach is useful for promoting dashboards from development to production or sharing standard layouts across teams.

## Best practices for sharing
<a name="observability-dashboards-sharing-best-practices"></a>
+ **Audience** – Design dashboards for a specific audience, such as on-call engineers or leadership.
+ **Focus** – Limit each dashboard to a single purpose or workflow.
+ **Conventions** – Use consistent naming conventions for dashboards and panels across your organization.
+ **Version control** – Export dashboard JSON definitions and store them in version control to track changes over time.
