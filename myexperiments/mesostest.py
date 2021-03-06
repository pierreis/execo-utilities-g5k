### THIS IS THE SCRIPT WE ARE GOING TO EXECUTE IN THE GRID5000 FRONTEND AND THE TEMPLATE FOR OUR EXPERIMENTS
### THIS SCRIPTS WILL BE PLACE INSIDE THE EXECO_UTILITIES_G5K root directory, possibly in a experiments folder and executed like py experiments/script.py
import sys
#   we add the paths in the frontend to be able to import SparkBench and the Experiment classes
## TODO: Add the paths in PYTHON environment variable so you can import directly.
sys.path.extend(["/home/abrandon/execo-g5k-benchmarks/spark"])
sys.path.extend(["/home/abrandon/execo-utilities-g5k"])
from sparkbench import SparkBench
from mesos_spark_experiment import MesosSparkExperiment

class SparkExperimentTestMesos(MesosSparkExperiment):
    def run(self):
        sb = SparkBench(home_directory="/home/abrandon/spark-bench/", master_node=self.masternode,
                    resource_manager="yarn",root_to_spark_submit="/opt/spark/bin/spark-submit",default_master="yarn")
        sb.create_all_bench_files(prefix="_first",size=10,npartitions=40,conf=[["spark.executor.memory","7g"]])
        sb.launch_all_apps(prefix="_first",conf=[["spark.executor.memory","5g"]])




if __name__ == '__main__':
    #dict = {"cluster":[("grimoire",1),("grisou",1)],"nodes":[(["griffon-17.nancy.grid5000.fr","griffon-16.nancy.grid5000.fr"],2)]}
    dict = {"cluster":[("graphene",3)]}
    walltime = "3:00:00"
    date=None
    experiment_name="spark_mesos_test"
    frontend="nancy"
    description="We want to experiment with Mesos and building a framework with it"
    mesos_experiment = SparkExperimentTestMesos("nancy",resources=dict,walltime=walltime,
                            date=date,experiment_name=experiment_name,description=description,ndatanodes=3,nnodemanagers=2,
                                                colocated=True,os_memory=2,nmasters=1)
    # TODO: All of this instructions can be wrapped in a method like .start()
    mesos_experiment.reserve_nodes()
    mesos_experiment.deploy_nodes()
    mesos_experiment.install()
    mesos_experiment.run()
    mesos_experiment.save_results()
    mesos_experiment.clean_job()