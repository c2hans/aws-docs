---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/entities-supply-planning.html
---

# Supply Planning
<a name="entities-supply-planning"></a>

The table below list the data entities and columns used by Supply Planning.

**Note**
**How to read the table:**
**Required** – The column name is mandatory in your dataset and you must populate the column name with values.
**Optional** – The column name is optional. For enhanced feature output, it is recommended to add the column name with values.
**Not required** – Data entity not required.

- ** [site](network-site-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** description / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** geo\_id / **Is the column used for Auto Replenishment?:** Required - Without this field, filters cannot group sites by category such as region, country, state, zip code and so on. / **Is the column used for Manufacturing Plan?:** Required - Without this field, filters cannot group sites by category such as region, country, state, zip code and so on.
  - **Column:** site\_type / **Is the column used for Auto Replenishment?:** NA / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** latitude / **Is the column used for Auto Replenishment?:** NA / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** longitude / **Is the column used for Auto Replenishment?:** NA / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** is\_active / **Is the column used for Auto Replenishment?:** Required - Identifies if a site needs to be considered for planning. Note, set the value to False if a site should not to be considered. If the field is kept blank or null, the site will be considered. / **Is the column used for Manufacturing Plan?:** Required - Identifies if a site needs to be considered for planning. Note, set the value to False if a site should not to be considered. If the field is kept blank or null, the site will be considered.
  - **Column:** open\_date / **Is the column used for Auto Replenishment?:** NA / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** end\_date / **Is the column used for Auto Replenishment?:** NA / **Is the column used for Manufacturing Plan?:** NA

- ** [transportation\_lane](network-transporation-lane-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** from\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** to\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** transit\_time / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** time\_uom / **Is the column used for Auto Replenishment?:** Required - Supported values include Day. / **Is the column used for Manufacturing Plan?:** Required - Supported values include Day.
  - **Column:** distance / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** distance\_uom / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** emissions\_per\_unit / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** emissions\_per\_weight / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** from\_geo\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** to\_geo\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** carrier\_tpartner\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** service\_type / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** trans\_mode / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** cost\_per\_unit / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** cost\_currency / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional

- ** [product](product-product-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** description / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Required - Without this field, filters cannot group by product category such as dairy, clothes, and so on. / **Is the column used for Manufacturing Plan?:** Required - Without this field, filters cannot group by product category such as dairy, clothes, and so on.
  - **Column:** is\_deleted / **Is the column used for Auto Replenishment?:** Required - Identifies if a product needs to be considered for planning. Set the field to False to consider this product and True to not consider the product. If this field is left blank or null, then the value will be defaulted to True. / **Is the column used for Manufacturing Plan?:** Required - Identifies if a product needs to be considered for planning. Set the field to False to consider this product and True to not consider the product. If this field is left blank or null, then the value will be defaulted to True.
  - **Column:** product\_type / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** parent\_product\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** base\_uom / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** unit\_cost / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** unit\_price / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional

- ** [product\_hierarchy](product-hierarchy-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** description / **Is the column used for Auto Replenishment?:** Required – This field is used by filters to group by a product category such as dairy, clothes, and so on. / **Is the column used for Manufacturing Plan?:** Required – This field is used by filters to group by a product category such as dairy, clothes, and so on.
  - **Column:** parent\_product\_group\_id / **Is the column used for Auto Replenishment?:** Optional – This field is used by filters to support multiple product category hierarchy such as dairy, full fat milk and so on. / **Is the column used for Manufacturing Plan?:** Optional – This field is used by filters to support multiple product category hierarchy such as dairy, full fat milk and so on.

- ** [geography](organization-geography-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** description / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** parent\_geo\_id / **Is the column used for Auto Replenishment?:** Optional – This field is used by filters to support multiple location hierarchy such as USA → USA-EAST. / **Is the column used for Manufacturing Plan?:** Optional – This field is used by filters to support multiple location hierarchy such as USA → USA-EAST.

- ** [trading\_partner](organization-trading-partner-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** description / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** country / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required – You must enter a value for eff\_start\_date and eff\_end\_date. If you don't have a value, enter **1900-01-01 00:00:00** for eff\_start\_date, and **9999-12-31 23:59:59** for eff\_end\_date. / **Is the column used for Manufacturing Plan?:** Required – You must enter a value for eff\_start\_date and eff\_end\_date. If you don't have a value, enter **1900-01-01 00:00:00** for eff\_start\_date, and **9999-12-31 23:59:59** for eff\_end\_date.
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required – You must enter a value for eff\_start\_date and eff\_end\_date. If you don't have a value, enter **1900-01-01 00:00:00** for eff\_start\_date, and **9999-12-31 23:59:59** for eff\_end\_date. / **Is the column used for Manufacturing Plan?:** Required – You must enter a value for eff\_start\_date and eff\_end\_date. If you don't have a value, enter **1900-01-01 00:00:00** for eff\_start\_date, and **9999-12-31 23:59:59** for eff\_end\_date.
  - **Column:** time\_zone / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** is\_active / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** tpartner\_type / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** geo\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.

- ** [inbound\_order](replenishment-inbound-order-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** order\_type / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** order\_status / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** to\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** submitted\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** tpartner\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.

- ** [inbound\_order\_line](replenishment-inbound-order-line-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** order\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** order\_type / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** status / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** to\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** from\_site\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** quantity\_submitted / **Is the column used for Auto Replenishment?:** Required – You must set one quantity field. / **Is the column used for Manufacturing Plan?:** Required – You must set one quantity field.
  - **Column:** quantity\_confirmed / **Is the column used for Auto Replenishment?:** Optional – You must set one quantity field. / **Is the column used for Manufacturing Plan?:** Optional – You must set one quantity field.
  - **Column:** quantity\_received / **Is the column used for Auto Replenishment?:** Optional – You must set one quantity field. / **Is the column used for Manufacturing Plan?:** Optional – You must set one quantity field.
  - **Column:** expected\_delivery\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** submitted\_date / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** incoterm / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** tpartner\_id / **Is the column used for Auto Replenishment?:** Required – This field is required for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – This field is required for successful ingestion.
  - **Column:** quantity\_uom / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** reservation\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** reference\_object\_type / **Is the column used for Auto Replenishment?:** Optional – This field is used for associating purchase order requests to purchase orders to track plan to PO conversion in the ERP. / **Is the column used for Manufacturing Plan?:** Optional – This field is used for associating purchase order requests to purchase orders to track plan to PO conversion in the ERP.
  - **Column:** reference\_object\_id / **Is the column used for Auto Replenishment?:** Optional – This field is used for associating purchase order requests to purchase orders to track plan to PO conversion in the ERP. / **Is the column used for Manufacturing Plan?:** Optional – This field is used for associating purchase order requests to purchase orders to track plan to PO conversion in the ERP.

- ** [inv\_policy](planning-inv-policy-entity.md) **
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** dest\_geo\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Optional – Either product\_id or product\_group\_id is required. / **Is the column used for Manufacturing Plan?:** Optional – Either product\_id or product\_group\_id is required.
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Optional – Either product\_id or product\_group\_id is required. / **Is the column used for Manufacturing Plan?:** Optional – Either product\_id or product\_group\_id is required.
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** ss\_policy / **Is the column used for Auto Replenishment?:** Required – The accepted values for this field are abs\_level, doc\_dem, doc\_fcst, and sl. / **Is the column used for Manufacturing Plan?:** Required – The accepted values for this field are abs\_level, doc\_dem, doc\_fcst, and sl.
  - **Column:** target\_inventory\_qty / **Is the column used for Auto Replenishment?:** Required – This field is required when ss\_policy is set to abs\_level. / **Is the column used for Manufacturing Plan?:** Required – This field is required when ss\_policy is set to abs\_level.
  - **Column:** target\_doc\_limit / **Is the column used for Auto Replenishment?:** Required – This field is required when ss\_policy is set to doc\_dem or doc\_fcst. / **Is the column used for Manufacturing Plan?:** Required – This field is required when ss\_policy is set to doc\_dem or doc\_fcst.
  - **Column:** target\_sl / **Is the column used for Auto Replenishment?:** Required – This field is required when ss\_policy is set to sl. / **Is the column used for Manufacturing Plan?:** Required – This field is required when ss\_policy is set to sl.

- ** [sourcing\_rules](planning-sourcing-rules-entity.md) **
  - **Column:** sourcing\_rule\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Optional – Either product\_id or product\_group\_id is required. / **Is the column used for Manufacturing Plan?:** Optional – Either product\_id or product\_group\_id is required.
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Optional – Either product\_id or product\_group\_id is required. / **Is the column used for Manufacturing Plan?:** Optional – Either product\_id or product\_group\_id is required.
  - **Column:** from\_site\_id / **Is the column used for Auto Replenishment?:** Optional – This field is required for sourcing\_rule types transfer. / **Is the column used for Manufacturing Plan?:** Optional – This field is required for sourcing\_rule types transfer.
  - **Column:** to\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** sourcing\_rule\_type / **Is the column used for Auto Replenishment?:** Required – The allowed values for this field are transfer, buy, and manufacture. / **Is the column used for Manufacturing Plan?:** Required – The allowed values for this field are transfer, buy, and manufacture. Only lower case is allowed.
  - **Column:** tpartner\_id / **Is the column used for Auto Replenishment?:** Optional – This field is required for sourcing\_rule types buy. / **Is the column used for Manufacturing Plan?:** Optional – This field is required for sourcing\_rule types buy.
  - **Column:** transportation\_lane\_id / **Is the column used for Auto Replenishment?:** Optional – This field is required for sourcing\_rule types transfer. / **Is the column used for Manufacturing Plan?:** Optional – This field is required for sourcing\_rule types transfer.
  - **Column:** production\_process\_id / **Is the column used for Auto Replenishment?:** Optional – This field is required for sourcing\_rule types manufacture. / **Is the column used for Manufacturing Plan?:** Optional – This field is required for sourcing\_rule types manufacture.
  - **Column:** sourcing\_priority / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** min\_qty / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** max\_qty / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** qty\_multiple / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required

- ** [sourcing\_schedule](planning-sourcing-schedule-entity.md)  This data entity is optional.  **
  - **Column:** sourcing\_schedule\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** tpartner\_id / **Is the column used for Auto Replenishment?:** Optional – This field is required for schedule\_type InboundOrdering. / **Is the column used for Manufacturing Plan?:** Optional – This field is required for schedule\_type InboundOrdering.
  - **Column:** status / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** from\_site\_id / **Is the column used for Auto Replenishment?:** Optional – This field is required for schedule\_type OutboundShipping. / **Is the column used for Manufacturing Plan?:** Optional – This field is required for schedule\_type OutboundShipping.
  - **Column:** to\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** schedule\_type / **Is the column used for Auto Replenishment?:** Required – The allowed values for this field are InboundOrdering and OutboundShipping. / **Is the column used for Manufacturing Plan?:** Required – The allowed values for this field are InboundOrdering and OutboundShipping.
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required

- ** [sourcing\_schedule\_details](planning-sourcing-schedule-details-entity.md)   This data entity is optional.  **
  - **Column:** sourcing\_schedule\_detail\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** sourcing\_schedule\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Optional – Either product\_id or product\_group\_id is required. / **Is the column used for Manufacturing Plan?:** Optional – Either product\_id or product\_group\_id is required.
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Optional – Either product\_id or product\_group\_id is required. / **Is the column used for Manufacturing Plan?:** Optional – Either product\_id or product\_group\_id is required.
  - **Column:** day\_of\_week / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** week\_of\_month / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** time\_of\_day / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional

- ** [product\_bom](planning-product-bom-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** production\_process\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** component\_product\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** component\_quantity\_per / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** assembly\_cost / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** assembly\_cost\_uom / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** priority / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required

- ** [production\_process](operation-production-process-entity.md) **
  - **Column:** production\_process\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** production\_process\_name / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** setup\_time / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** setup\_time\_uom / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** operation\_time / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** operation\_time\_uom / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Optional

- ** [inv\_level](inventory_mgmnt-inv-level-entity.md) **
  - **Column:** snapshot\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** on\_hand\_inventory / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** allocated\_inventory / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** bound\_inventory / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** lot\_number / **Is the column used for Auto Replenishment?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** expiry\_date / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required

- ** [forecast](forecast-forecast-entity.md) **
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** mean / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** p10 / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** p50 / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** p90 / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** forecast\_start\_dttm / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** forecast\_end\_dttm / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** snapshot\_date / **Is the column used for Auto Replenishment?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** region\_id / **Is the column used for Auto Replenishment?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.

- ** [vendor\_product](vendor-management-product-entity.md) **
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** vendor\_tpartner\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required

- ** [vendor\_lead\_time](vendor-management-lead-time-entity.md) **
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** vendor\_tpartner\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** planned\_lead\_time / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** region\_id / **Is the column used for Auto Replenishment?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.

- ** [outbound\_order\_line](outbound-fulfillment-order-line-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required – This field determines the outbound shipment id. / **Is the column used for Manufacturing Plan?:** Required – This field determines the outbound shipment id.
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required – This field determines the id of the product shipped. / **Is the column used for Manufacturing Plan?:** Required – This field determines the id of the product shipped.
  - **Column:** cust\_order\_id / **Is the column used for Auto Replenishment?:** Required – This field determines the id of the outbound order. / **Is the column used for Manufacturing Plan?:** Required – This field determines the id of the outbound order.
  - **Column:** ship\_from\_site\_id / **Is the column used for Auto Replenishment?:** Required – This field determines the site from where the product units are requested. / **Is the column used for Manufacturing Plan?:** Required – This field determines the site from where the product units are requested.
  - **Column:** ship\_to\_site\_id / **Is the column used for Auto Replenishment?:** Not required / **Is the column used for Manufacturing Plan?:** Not required
  - **Column:** init\_quantity\_requested / **Is the column used for Auto Replenishment?:** Optional – This field determines the final quantity after any cancellations and changes. / **Is the column used for Manufacturing Plan?:** Optional – This field determines the final quantity after any cancellations and changes.
  - **Column:** quantity\_promised / **Is the column used for Auto Replenishment?:** Optional – This field displays the promised quantity. / **Is the column used for Manufacturing Plan?:** Optional – This field displays the promised quantity.
  - **Column:** quantity\_delivered / **Is the column used for Auto Replenishment?:** Optional – This field displays the actual quantity delivered. / **Is the column used for Manufacturing Plan?:** Optional – This field displays the actual quantity delivered.
  - **Column:**  final\_quantity\_requested  / **Is the column used for Auto Replenishment?:** Optional – Final quantity after any cancellations or changes  / **Is the column used for Manufacturing Plan?:** Optional – Final quantity after any cancellations or changes
  - **Column:** status / **Is the column used for Auto Replenishment?:** Optional – This field determines the status of the order line, that is, canceled, open, closed, and so on. / **Is the column used for Manufacturing Plan?:** Optional – This field determines the status of the order line, that is, canceled, open, closed, and so on.
  - **Column:** requested\_delivery\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** promised\_delivery\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** actual\_delivery\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional

- ** [segmentation](planning-segmentation-entity.md) **
  - **Column:** segment\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** creation\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** company\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** segment\_description / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** segment\_type / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** segment\_value / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** source / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required

- ** [company](organization-company-entity.md)  This data entity is optional.  **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** description / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** address\_1 / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** address\_2 / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** address\_3 / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** city / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** state\_prov / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** postal\_code / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** country / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** phone\_number / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** time\_zone / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** calendar\_id / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional

- ** [supply\_planning\_paramters](planning-supply_planning_parameters-entity.md)  This data entity is optional.  **
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** product\_group\_id / **Is the column used for Auto Replenishment?:** Required. For future Use. Please populate SCN\_RESERVED\_NO\_VALUE\_PROVIDED for now. / **Is the column used for Manufacturing Plan?:** Required. For future Use. Please populate SCN\_RESERVED\_NO\_VALUE\_PROVIDED for now.
  - **Column:** site\_id / **Is the column used for Auto Replenishment?:** Required. For future Use. Please populate SCN\_RESERVED\_NO\_VALUE\_PROVIDED for now. / **Is the column used for Manufacturing Plan?:** Required. For future Use. Please populate SCN\_RESERVED\_NO\_VALUE\_PROVIDED for now.
  - **Column:** planner\_name / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** Optional
  - **Column:** demand\_time\_fence\_days / **Is the column used for Auto Replenishment?:** Optional.For future use / **Is the column used for Manufacturing Plan?:** Optional.For future use
  - **Column:** forecast\_consumption\_backward\_days / **Is the column used for Auto Replenishment?:** Optional.For future use / **Is the column used for Manufacturing Plan?:** Optional.For future use
  - **Column:** forecast\_consumption\_forward\_days / **Is the column used for Auto Replenishment?:** Optional.For future use / **Is the column used for Manufacturing Plan?:** Optional.For future use
  - **Column:** eff\_start\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required
  - **Column:** eff\_end\_date / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** Required

- ** [shipment](replenishment-shipment-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** ship\_to\_site\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** ship\_from\_site\_id / **Is the column used for Auto Replenishment?:** Required – Supply Planning can use the value from *ship\_from\_site\_id* or *supplier\_tpartner\_id*. / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** supplier\_tpartner\_id / **Is the column used for Auto Replenishment?:** Required – Supply Planning can use the value from *ship\_from\_site\_id* or *supplier\_tpartner\_id*. / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** order\_type / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** units\_shipped / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** planned\_delivery\_date / **Is the column used for Auto Replenishment?:** Required – Supply Planning can use the value from *planned\_delivery\_date*, *actual\_delivery\_date*, or *carrier\_eta\_date*. / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** actual\_delivery\_date
  - **Column:** carrier\_eta\_date
  - **Column:** planned\_ship\_date / **Is the column used for Auto Replenishment?:** Required – Supply Planning can use the value from *planned\_ship\_date*, or *actual\_ship\_date*. / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** actual\_ship\_date
  - **Column:** creation\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** shipment\_status / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** order\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** order\_line\_id
  - **Column:** package\_id

- ** [shipment\_lot](replenishment-shipment-lot-entity.md) **
  - **Column:** id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** lot\_qty / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** expiry\_date / **Is the column used for Auto Replenishment?:** Optional / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** shipment\_id / **Is the column used for Auto Replenishment?:** Required / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** product\_id / **Is the column used for Auto Replenishment?:** Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion. / **Is the column used for Manufacturing Plan?:** NA
  - **Column:** tpartner\_id
  - **Column:** order\_id
  - **Column:** order\_line\_id
  - **Column:** package\_id
