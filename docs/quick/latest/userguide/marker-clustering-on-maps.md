---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/marker-clustering-on-maps.html
---

# Marker clustering on geospatial point maps in Quick
<a name="marker-clustering-on-maps"></a>

Use marker clustering to improve readability of collocated points on a map. Geospatial locations on point maps are represented using markers. Usually, there is one marker per data point. However, if there are too many markers close together, the map becomes difficult to read. To make it easier to interpret the map, you can enable marker clustering to represent groupings of locations on the map. As the reader zooms in on the map, the clustered markers leave the area marker to display separately.

![This is an example of marker clustering at work.](http://docs.aws.amazon.com/quick/latest/userguide/images/map-marker-clustering.gif)

**To add cluster points to a map**

1. Open your analysis, and choose the geospatial map that you want to format. When you select a visual, it displays with a highlight around it.

1. To open the formatting pane, select the **Format visual** icon from the on-visual menu.

1. On the formatting pane at left, choose **Points**.

1. Choose one of the following options:
   + **Basic** – use the default display setting for map points.
   + **Cluster points** – cluster map points together when there are many in one area.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
