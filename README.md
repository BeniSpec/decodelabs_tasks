# Decode Labs — Data Analytics Internship Tasks

This repo contains my submissions for the Decode Labs Data Analytics internship:

- **Project 1** — Data Cleaning & Preparation
- **Project 2** — Exploratory Data Analysis
- **Project 3** — SQL Data Analysis

All three projects use the same e-commerce orders dataset, so the work
builds from one project into the next.

## A Note on Query Order
SQL doesn't run top to bottom the way you read it. The database
processes FROM and WHERE before SELECT, which is why you can't
filter using a column alias you just created in SELECT — that alias
doesn't exist yet at the point WHERE runs.