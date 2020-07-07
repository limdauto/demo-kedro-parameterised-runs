# demo-kedro-parameterised-runs

This is an example Kedro pipeline that allows you to parameterise each pipeline run with different input and output.

In the [data/01_raw](./data/01_raw) folder, you will find multiple CSV files. To run the pipeline with each of these files, use:

```bash
kedro run --params=input:<filename>.csv
```

It will also create a corresponding output file in [data/08_reporting](./data/08_reporting). This is made possible by the [`before_pipeline_run` hook implementation](./src/demo_kedro_parameterised_runs/hooks.py), which dynamically adds an input and output dataset to the catalog using the given filename.

To loop through the files and run the pipeline once per file, use the following simple bash script:

```bash
for input in data/01_raw/*
do
    file=$(basename $input)
    kedro run --params=input:"$file"
done
```
