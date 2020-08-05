# 文章对比接口说明

## 架构

![image-20200805145320764](https://gitee.com/gsunwu/blogs/raw/master/blogs-images/20200805145320.png)



## RestFul API

测试host：	http://sunwu.zicp.net/

### **文章对比** 

#####  POST /v1/html 

##### req

```
{
  "type": "html",  
  "distance":20,  
  "papers": [   
    {
      "name": "zhangsan",
      "sno": "2019201964",
      "papername": "if i was a boy",
      "content":"<h1>if i was a boy, i will go to fly like a bird</h1>"
    },
       {
      "name": "zhangsan",
      "sno": "2019201963",
      "papername": "if i was a boy",
      "content":"<h1>if i was a boy, i will go to fly like a bird</h1>"
    },
       {
      "name": "zhangsan",
      "sno": "2019201962",
      "papername": "if i was a boy",
      "content":"<h1>if i was a boy, i will go to fly like a bird</h1>"
    }
  ]
}
```

##### res

```
{
    "code": 200,
    "type": "success",
    "msg": "",
    "data": {
        "2019201964": [ # 本篇文章为2019201964 ，与其他文章的对比
            {
                "name": "zhangsan", # 本篇文章的姓名
                "sno": "2019201964", #本篇文章的sno
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": -1 # -1 表示表本篇文章
            },
            # 以下为对比的文章
            {
                "name": "zhangsan",
                "sno": "2019201963",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": 0,
                "percent": 100.0 ## 文章的相似的可能性，0-100
            },
            {
                "name": "zhangsan",
                "sno": "2019201962",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": 0,
                "percent": 100.0
            }
        ],
        "2019201963": [
            {
                "name": "zhangsan",
                "sno": "2019201963",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": -1
            },
            {
                "name": "zhangsan",
                "sno": "2019201964",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": 0,
                "percent": 100.0
            },
            {
                "name": "zhangsan",
                "sno": "2019201962",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": 0,
                "percent": 100.0
            }
        ],
        "2019201962": [
            {
                "name": "zhangsan",
                "sno": "2019201962",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": -1
            },
            {
                "name": "zhangsan",
                "sno": "2019201964",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": 0,
                "percent": 100.0
            },
            {
                "name": "zhangsan",
                "sno": "2019201963",
                "papername": "if i was a boy",
                "content": "<h1>if i was a boy, i will go to fly like a bird</h1>",
                "distance": 0,
                "percent": 100.0
            }
        ]
    }
}
```

##### note

```
  "type": "html", // 文章类型
  "distance":20,  //判定距离
  "papers": [     //文章
```

