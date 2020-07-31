option = {
    title: {
        text: 'Graph 简单示例'
    },
    tooltip: {},
    animationDurationUpdate: 15000,
    animationEasingUpdate: 'quinticInOut',
    series: [
        {
            type: 'graph',
            layout: 'none',
            roam: true,
            symbolSize: 50,// 决定全局图像的大小，如圆
            label: {
                show: true
            },
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [4, 10],
            edgeLabel: {
                fontSize: 20
            },
            data: [{
                symbolSize: 100, // 决定当前图形的大小
                name: '节点1',
                x: 300,
                y: 300
            }, {
                name: '节点2',
                x: 800,
                y: 300
            }, {
                name: '节点3',
                x: 550,
                y: 100
            }, {
                name: '节点4',
                x: 550,
                y: 500
            },
             {
                name: '节点5',
                x: 550,
                y: 600
            }],
            // links: [],
            links: [{
                source: '节点1', // source 和 target 表示端点，由data: [{name: '节点1' 指定
                target: '节点3',
                symbolSize: [20, 1], //第一个参数决定箭头起始的圆滑程度，第二个参数决定箭头的大小，只是箭头
                label: {
                    show: true //是否展示文字【 source > target 】
                },
                lineStyle: {
                    width: 20, // 连接线的宽度
                    curveness:0.5 // 连接线的弯曲程度
                }
            }, {
                source: '节点2',
                target: '节点1',
                label: {
                    show: true
                },
                lineStyle: {
                    curveness: 1.2
                }
            }, {
                source: '节点1',
                target: '节点3'
            }, {
                source: '节点2',
                target: '节点3'
            }, {
                source: '节点2',
                target: '节点4'
            }, {
                source: '节点1',
                target: '节点4'
            }, {
                source: '节点1',
                target: '节点5'
            }],
            lineStyle: {
                opacity: 0.9,
                width: 2,
                curveness: 0
            }
        }
    ]
};