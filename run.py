from spark_experiment import *

if __name__ == '__main__':
    #dict = {"cluster":[("grimoire",1),("grisou",1)],"nodes":[(["griffon-17.nancy.grid5000.fr","griffon-16.nancy.grid5000.fr"],2)]}
    dict = {"cluster":[("grimoire",1),("grisou",1),("griffon",3)]}
    walltime = "2:25:00"
    date=None
    experiment_name="execo_test"
    frontend="nancy"
    spark_experiment = SparkExperiment("nancy",resources=dict,walltime=walltime,date=None,experiment_name=experiment_name,nDatanodes=5,nNodemanagers=4,colocated=True,os_memory=2)
    spark_experiment.reserve_nodes()
    spark_experiment.deploy_nodes()
    spark_experiment.install()
    spark_experiment.clean_job()