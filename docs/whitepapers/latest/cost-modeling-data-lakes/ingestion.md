---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/ingestion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Ingestion
<a name="ingestion"></a>

 Services required for ingestion depend on the source of data, the frequency at which the data should be consumed for processing to derive business value from it, and the data transfer rate.

## Cost factors
<a name="ingestion-cost-factors"></a>

 Depending on the services you choose, the primary cost factors are:
+  **Storage** – These are the costs you pay for storing your raw data as it arrives.
+  **Data transfer** – These are the costs you pay for moving the data. Costs can be either bandwidth charges, leased line, or offline transfer. It is worth noting the analytics services should be deployed in the same Region to avoid unnecessary inter-Region data transfer. This improves performance and reduces costs.
+  **Managed service costs** – These are the costs you pay (usually per second or per hour) for the service you are using, if you chose a managed service from AWS (for example, AWS IoT or AWS Transfer for SFTP).
