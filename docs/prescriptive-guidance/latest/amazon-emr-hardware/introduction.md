---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/introduction.html
---

# Choosing the hardware for your Amazon EMR cluster
<a name="introduction"></a>

*Sayde Aguilar, Amiin Samatar, Diego Valencia, and Sunil Yadav, Amazon Web Services*

Amazon EMR is a tool for big data processing. It uses open source software, specifically Apache tools such as Apache Spark and Apache Hudi. In addition, it offers several options for configuring and using a low-cost, pay-as-you-go model.

## Overview
<a name="overview"></a>

Amazon EMR is built using Apache Hadoop MapReduce, a framework for processing vast amounts of data. Hadoop MapReduce processes the data in distributed clusters at the same time using parallel logic, which means every process has its own processor. Amazon EMR uses a Hadoop cluster of virtual servers structured on Amazon Elastic Compute Cloud (Amazon EC2). This means all the parallel processes are made on standalone computers running on Amazon Web Services (AWS).

A Hadoop cluster is a specific type of computational cluster that is used for processing large amounts of unstructured data using parallel or distributed environments. A key characteristic of a Hadoop cluster it that it is highly scalable and can be configured to increase the velocity of data processing. The scalability is reached by adding or removing nodes to increase or decrease the throughput. On Hadoop clusters, each piece of data is copied between cluster nodes, so there is close to zero data lost if a node fails.

On Amazon EMR, *elasticity* refers to the dynamic resizing ability. You can automatically scale the cluster and make any changes that you need. You don't have to rely on your initial hardware design.

This guide explains how to design your Amazon EMR cluster based on that elasticity, and it provides best practices to follow when choosing the hardware.
