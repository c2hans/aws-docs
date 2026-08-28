---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-satellite-classification.html
---

# Classify satellite imagery in parallel on Deadline Cloud
<a name="examples-jb-satellite-classification"></a>

The [satellite\_classification](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/satellite_classification) job bundle classifies satellite image tiles into land-cover categories (water, vegetation, bare soil, rock, cloud) and merges the results into a single map. The classifier reads color ratios between the four spectral bands of each tile to decide what's on the ground.

The job runs in two steps. `ClassifyTiles` fans out one parallel task per tile that downloads the tile, classifies its pixels, and writes a result file plus a color PNG. `MosaicResults` runs after the parallel step finishes and merges every tile into one map plus an overview image with class percentages. This fan-out and merge pattern applies to any workload where input files are independent.

The bundle ships with five sample tiles simulating the Grand Canyon area. They're downloaded automatically from the Deadline Cloud samples CDN when the job runs — no external data or accounts needed.

The bundle requires a farm with a conda queue environment that has `conda-forge` in the channel list (the classifier uses the `rasterio` package). The quickest setup is the [starter farm AWS CloudFormation (CloudFormation) template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm) — set its `ProdCondaChannels` parameter to `deadline-cloud conda-forge`.

Submit with the sample tiles:

```
deadline bundle submit job_bundles/satellite_classification/
```

To classify your own tiles, point `TilesDir` at a local directory of 4-band `.tif` files:

```
deadline bundle submit job_bundles/satellite_classification/ \
  -p TilesDir={{path-to-tiles}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
