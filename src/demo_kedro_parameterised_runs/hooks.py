from kedro.extras.datasets.pandas import CSVDataSet
from kedro.extras.datasets.text import TextDataSet
from kedro.framework.hooks import hook_impl

from typing import Any, Dict


class PipelineHooks:

    @hook_impl
    def before_pipeline_run(self, run_params: Dict[str, Any], pipeline, catalog):
        """A hook implementation to add a catalog entry
        based on the filename passed to the command line, e.g.:
            kedro run --params=input:iris_1.csv
            kedro run --params=input:iris_2.csv
            kedro run --params=input:iris_3.csv
        """
        filename = run_params["extra_params"]["input"]

        # add input dataset
        input_dataset_name = "example_iris_data"
        input_dataset = CSVDataSet(filepath=f"data/01_raw/{filename}")
        catalog.add(input_dataset_name, input_dataset)

        # add output dataset
        output_dataset_name = "example_reporting_data"
        output_dataset = TextDataSet(filepath=f"data/08_reporting/{filename}")
        catalog.add(output_dataset_name, output_dataset)
