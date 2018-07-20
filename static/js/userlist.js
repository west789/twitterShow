layui.use(['laypage', 'layer', 'table', 'jquery'], function () {
    var table = layui.table;
    var $ = layui.jquery;
    table.on('tool(fi_check)', function (obj) {
        var data = obj.data;
        if (obj.event === 'detail') {
            window.location.href="/show/detailaccount/"+data.accountId
        }
    });
    table.render({
        elem: "#tbl_userlist",
        height: 630,
        // url: "/satic/json/data.json",
        url: "/show/get_userlist/",
        page: true,
        limit: 20,
        skin: "line",
        even: true,
        cols: [
            [ //表头
                {
                    field: 'accountId',
                    title: '编号',
                    width: 100,
                    sort: true,
                    fixed: 'left'
                }, {
                field: 'accountName',
                title: '账户昵称',
                width: 200
            }, {
                field: 'screenName',
                title: '账户号',
                width: 200,
                // sort: true
            }, {
                field: 'statusesCount',
                title: '推文',
                width: 200,
                // sort: true
            }, {
                field: 'friendsCount',
                title: '正在关注',
                width: 200
            }, {
                field: 'favoritesCount',
                title: '喜欢',
                width: 200
            }, {
                field: 'followersCount',
                title: '关注者',
                width: 100
            }, {
                field: 'accountTime',
                title: '成立时间',
                width: 200
            }, {
                title: '操作',
                fixed: 'right',
                // width: 165,
                align: 'center',
                toolbar: '#barDemo'
            }

            ]
        ]
    });
})