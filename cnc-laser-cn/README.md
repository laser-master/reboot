# Redsail 激光设备中文网站

这是Redsail激光设备的中文官方网站项目，基于原有 redsail-laser.com 网站内容重新设计和开发。

## 项目概述

本项目旨在为Redsail激光设备创建一个现代化的、响应式的中文网站，提供完整的产品信息、公司介绍和客户服务功能。

### 项目目标

- **品牌展示**: 全面展示Redsail作为专业激光设备制造商的形象
- **产品营销**: 详细介绍激光切割机、雕刻机、配件耗材和软件系统
- **客户服务**: 提供在线咨询、技术支持和售后服务信息
- **市场拓展**: 更好地服务中文市场，提升品牌影响力
- **内容迁移**: 在获得适当权限后，迁移和优化 redsail-laser.com 的内容

## 技术栈

- **前端框架**: 纯HTML5 + CSS3 + Vanilla JavaScript
- **响应式设计**: Mobile-first设计，支持多种设备
- **样式系统**: CSS自定义属性（CSS变量）+ Flexbox + Grid
- **图标字体**: Emoji + Unicode符号
- **构建工具**: 无需构建，直接部署静态文件

## 项目结构

```
cnc-laser-cn/
├── index.html              # 主页
├── about.html              # 关于我们
├── contact.html            # 联系我们
├── products/               # 产品中心
│   ├── index.html          # 产品总览
│   ├── cutting-machines/   # 激光切割机
│   │   └── index.html
│   ├── engraving-machines/ # 激光雕刻机
│   │   └── index.html
│   ├── accessories/        # 配件耗材
│   │   └── index.html
│   └── software/           # 软件系统
│       └── index.html
├── assets/                 # 静态资源
│   ├── css/               # 样式文件
│   │   ├── main.css       # 主要样式
│   │   └── components.css # 组件样式
│   ├── images/            # 图片资源
│   ├── js/                # JavaScript文件
│   │   └── main.js        # 主要功能
│   └── docs/              # 文档资源
└── README.md              # 项目说明
```

## 功能特性

### 🏠 主页 (index.html)
- 品牌展示和核心价值主张
- 主要产品类别预览
- 公司优势特点介绍
- 客户案例和应用领域

### 🏢 关于我们 (about.html)
- 公司发展历程和时间线
- 企业文化和核心价值观
- 团队实力和统计数据
- 公司里程碑事件

### 📞 联系我们 (contact.html)
- 详细联系信息和办公地址
- 在线询价表单
- 服务区域覆盖
- 常见问题解答
- 地图位置（待集成）

### 🛠️ 产品中心 (products/)

#### 产品总览 (products/index.html)
- 所有产品类别的概览
- 技术规格对比表
- 应用行业展示

#### 激光切割机 (products/cutting-machines/)
- 光纤激光切割机系列
- CO2激光切割机系列
- 混合激光切割机系列
- 自动上下料系统
- 产品详细规格和应用

#### 激光雕刻机 (products/engraving-machines/)
- CO2激光雕刻机
- 光纤激光打标机
- UV激光雕刻机
- 便携式雕刻设备

#### 配件耗材 (products/accessories/)
- 激光管和激光器
- 光学镜片（聚焦镜、反射镜）
- 激光头组件
- 喷嘴和消耗品
- 维护保养服务

#### 软件系统 (products/software/)
- LaserCut控制软件
- CAM编程软件
- 设计软件插件
- 生产管理系统

### 🎨 设计特色

- **现代化设计**: 简洁、专业的企业级设计风格
- **响应式布局**: 支持桌面、平板和移动设备
- **品牌一致性**: 与Redsail品牌标识保持一致
- **用户体验**: 直观的信息架构和导航
- **性能优化**: 轻量级代码，快速加载

## 开发与部署

### 开发环境要求
- 现代浏览器（Chrome、Firefox、Safari、Edge）
- 代码编辑器（VS Code推荐）
- 本地HTTP服务器（用于测试）

### 本地开发

1. **克隆项目**
   ```bash
   # 项目已在当前仓库中，位于 cnc-laser-cn/ 目录
   ```

2. **启动本地服务器**
   ```bash
   # 使用Python
   python -m http.server 8000
   
   # 使用Node.js
   npx serve .
   
   # 使用PHP
   php -S localhost:8000
   ```

3. **访问网站**
   打开浏览器访问 `http://localhost:8000`

### 部署说明

#### 静态网站部署
由于这是纯静态网站，可以部署到任何静态网站托管服务：

- **Vercel**: 连接GitHub仓库自动部署
- **Netlify**: 拖拽文件夹或连接Git仓库
- **GitHub Pages**: 在仓库设置中启用
- **阿里云OSS**: 静态网站托管
- **腾讯云COS**: 静态网站托管
- **传统虚拟主机**: 通过FTP上传文件

#### 部署步骤

1. **准备文件**
   ```bash
   # 确保所有文件都在 cnc-laser-cn/ 目录中
   ls -la cnc-laser-cn/
   ```

2. **上传文件**
   ```bash
   # 使用rsync同步到服务器
   rsync -avz --delete cnc-laser-cn/ user@server:/path/to/webroot/
   ```

3. **配置服务器**
   - 设置默认索引文件为 `index.html`
   - 配置GZIP压缩
   - 设置缓存策略
   - 配置HTTPS（推荐）

### 环境配置

#### Apache (.htaccess)
```apache
# 启用GZIP压缩
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# 设置缓存
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
</IfModule>

# 安全头
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"
```

#### Nginx
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /path/to/cnc-laser-cn;
    index index.html;
    
    # GZIP压缩
    gzip on;
    gzip_types text/plain text/css application/javascript application/json;
    
    # 静态资源缓存
    location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    # HTML文件缓存
    location ~* \.html$ {
        expires 1h;
        add_header Cache-Control "public";
    }
    
    # 安全头
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
}
```

## 内容迁移指南

### 从 redsail-laser.com 迁移内容

⚠️ **重要**: 在进行内容迁移之前，请确保获得适当的版权和使用权限。

#### 内容迁移步骤

1. **内容审核**
   - 审核原网站的所有内容
   - 识别需要迁移的文本内容
   - 检查图片和多媒体资源的使用权限
   - 更新过时或错误的信息

2. **内容转换**
   - 将英文内容翻译为中文
   - 调整内容结构以适应新设计
   - 更新产品规格和参数
   - 刷新公司信息和联系方式

3. **SEO优化**
   - 更新meta标签和描述
   - 优化页面标题和URL结构
   - 添加结构化数据标记
   - 创建XML站点地图

4. **图片资源**
   - 压缩和优化图片文件
   - 更新图片alt文本
   - 确保图片符合版权要求
   - 添加WebP格式支持

#### 内容映射表

| 原网站内容 | 新网站位置 | 状态 |
|------------|------------|------|
| 首页横幅 | index.html hero区域 | ✅ 已创建 |
| 产品目录 | products/index.html | ✅ 已创建 |
| 公司介绍 | about.html | ✅ 已创建 |
| 联系方式 | contact.html | ✅ 已创建 |
| 产品详情 | products/cutting-machines/ 等 | ✅ 已创建 |

### 版权注意事项

- ✅ 重新创建的内容没有版权问题
- ⚠️ 使用原网站内容需要获得授权
- ⚠️ 产品图片需要确认版权状况
- ⚠️ 技术文档需要原作者同意

## 浏览器兼容性

| 浏览器 | 最低版本 | 测试状态 |
|--------|----------|----------|
| Chrome | 80+ | ✅ 已测试 |
| Firefox | 75+ | ✅ 已测试 |
| Safari | 13+ | ✅ 已测试 |
| Edge | 80+ | ✅ 已测试 |
| IE | 不支持 | ❌ 不兼容 |

## 性能优化

### 已实现的优化

- **CSS优化**: 使用CSS变量和高效选择器
- **JavaScript优化**: 事件委托和防抖节流
- **图片优化**: 使用适当的图片格式和大小
- **代码压缩**: 移除不必要的空白和注释

### 性能指标

- **首次内容绘制 (FCP)**: < 1.5s
- **最大内容绘制 (LCP)**: < 2.5s
- **累积布局偏移 (CLS)**: < 0.1
- **首次输入延迟 (FID)**: < 100ms

## 维护与更新

### 内容更新

1. **产品信息更新**
   - 更新产品规格和价格
   - 添加新产品或停产旧产品
   - 修改产品图片和描述

2. **公司信息更新**
   - 更新联系方式和地址
   - 添加新的团队成员
   - 更新公司新闻和事件

3. **技术文档更新**
   - 更新用户手册
   - 添加新的软件版本
   - 修改安装指南

### 版本控制

- 使用Git进行版本控制
- 遵循语义化版本命名
- 创建详细的提交信息
- 使用分支进行功能开发

## 扩展功能规划

### 近期计划 (v1.1)
- [ ] 集成真实地图服务
- [ ] 添加多语言支持
- [ ] 优化移动端体验
- [ ] 集成客服系统

### 中期计划 (v1.2)
- [ ] 添加产品配置器
- [ ] 集成在线客服
- [ ] 添加用户注册功能
- [ ] 创建客户门户

### 长期计划 (v2.0)
- [ ] 重构为React/Vue应用
- [ ] 集成CMS系统
- [ ] 添加电商功能
- [ ] 创建移动应用

## 技术支持

### 联系方式

- **开发团队**: [待更新]
- **技术文档**: 参见 `/docs/` 目录
- **问题反馈**: [待更新]

### 常见问题

**Q: 如何添加新产品？**
A: 在相应产品类别目录中创建新的HTML文件，参考现有产品页面的结构。

**Q: 如何修改网站颜色主题？**
A: 编辑 `/assets/css/main.css` 中的CSS变量部分。

**Q: 如何添加新的语言版本？**
A: 创建新的目录结构，如 `en/` 表示英文版，`ja/` 表示日文版。

**Q: 网站支持哪些支付方式？**
A: 当前版本为展示型网站，支付功能将在后续版本中集成。

## 许可证

本项目基于特定许可证发布，具体许可证信息请参见项目根目录的LICENSE文件。

---

**最后更新**: 2024年12月13日  
**版本**: 1.0.0  
**维护者**: Redsail 开发团队