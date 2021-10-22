1. gmv_cost1：过滤了smart_optimization_goal not in(0, 6, 7, 10)，second_goal != 106 

2. gmv_cost2：smart_optimization_goal !=0

   ![image-20210610223507342](https://tva1.sinaimg.cn/large/008i3skNgy1grdjor3ljlj30ou08p75g.jpg)

3. gmv_cost3：在2的基础上，字段全部用有效前缀的

   ![image-20210610223425267](https://tva1.sinaimg.cn/large/008i3skNgy1grdjo2aqr4j30hy0a8q4d.jpg)

4. gmv_cost4：smart_optimization_goal = 104，second_goal=0

   ![wecom-temp-5cd98021296b873f857ed79da1e8ff4c](https://tva1.sinaimg.cn/large/008i3skNgy1grec77olhpj30cr07gwf6.jpg)

   ​	全对上了

5. gmv_cost5：smart_optimization_goal = 104

   ![image-20210611171846843](https://tva1.sinaimg.cn/large/008i3skNgy1greg5wntupj30dv092gmp.jpg)

   除了gmv，其他的都对上了

6. gmv_cost6：smart_optimization_goal = 104，second_goal=0 union second_goal!=0

   ![image-20210611180725127](https://tva1.sinaimg.cn/large/008i3skNgy1grehkij0arj30c40bfmyb.jpg)

   除了gmv，其他的都对上了

7. gmv_cost7：smart_optimization_goal != 0，second_goal=0unionsecond_goal!=0

   ![image-20210611182703531](https://tva1.sinaimg.cn/large/008i3skNgy1grei4y3v7gj30el0bbq4f.jpg)

   gmv与pcvr_bias都不对

8. gmv_cost8：smart_optimization_goal = 104，second_goal=0 ，case second_goal

   ![image-20210611193905590](https://tva1.sinaimg.cn/large/008i3skNgy1grek7w3rvhj30dm0bgjsu.jpg)

   9. gmv_cost9：smart_optimization_goal = 104，case second_goal

   10. gmv_cost10：adgroup_id = 290994061

       

   