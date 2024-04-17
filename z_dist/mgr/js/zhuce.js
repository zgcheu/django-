// 等待文档加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 获取国家下拉菜单元素
    var countryDropdown = document.getElementById('myDropdown');

    // 获取下拉菜单项的容器
    var menuContainer = document.getElementById('menuItems');

    // 添加国家下拉菜单点击事件监听器
    countryDropdown.addEventListener('click', function(event) {
        // 发送 GET 请求到后端获取国家列表
        fetch('/api/mgr/country', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            // 获取后端返回的国家列表
            const countries = data.countries;

            // 清空菜单容器
            menuContainer.innerHTML = '';

            // 将后端返回的国家列表添加到菜单容器中
            countries.forEach(country => {
                const menuItem = document.createElement('a');
                menuItem.textContent = country.name;
                menuItem.addEventListener('click', function() {
                    // 更新国家显示的内容为所选菜单项的内容
                    countryDropdown.querySelector('span').textContent = country.name;
                    // 隐藏下拉菜单
                    menuContainer.style.display = 'none';

                    // 隐藏其他选项，只显示被选择的选项
                    menuContainer.childNodes.forEach(node => {
                        if (node.textContent !== country.name) {
                            node.style.display = 'none';
                        } else {
                            node.style.display = 'block';
                        }
                    });
                });
                menuContainer.appendChild(menuItem);
            });

            // 显示下拉菜单
            menuContainer.style.display = 'block';
        })
        .catch(error => {
            // 请求失败，打印错误信息
            console.error('Error:', error);
        });
    });

    // 添加文档点击事件监听器，用于在点击其他地方时隐藏下拉菜单
    document.addEventListener('click', function() {
        // 隐藏下拉菜单
        menuContainer.style.display = 'none';
    });

    // 阻止点击下拉菜单项时事件冒泡，以防止隐藏下拉菜单
    menuContainer.addEventListener('click', function(event) {
        event.stopPropagation();
    });

    // 注册用户函数
    function submit1() {
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
        var conf_password = document.getElementById('conf_password').value;

        // 检查密码是否与确认密码匹配
        if (password !== conf_password) {
            alert("密码与确认密码不匹配");
            return;
        }

        // 构造要发送给后端的数据
        var requestData = {
            username: username,
            password: password, // 将密码添加到发送的数据中
            country: countryDropdown.querySelector('span').textContent // 获取选择的国家
        };

        // 发送POST请求
        fetch('/api/mgr/index', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            // 处理从后端返回的响应数据
            if (data.success === "User registered successfully") {
                // 注册成功，重定向到登录页面
                window.location.href = '/mgr/html/sign.html';
            } else {
                // 注册失败，提示错误信息并清空输入框
                alert('注册失败，请您重试！');
                username = '';
                password = '';
            }
        })
        .catch(error => {
            // 请求失败，打印错误信息
            console.error('Error:', error);
        });
    }

    // 在控制台输出点击成功
    console.log('Script loaded successfully!');
});




