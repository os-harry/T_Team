// pages/class_create/class_create.js
var app=getApp(); //初始化它以使用app.js中的全局变量

Page({
  data: {
    class_id: 1 //随便放一个，后面onload的时候会用全局的class_id来修改
  },
  //表单提交
  formSubmit: function (e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
    wx.request({
      url: 'http://127.0.0.1:5000/test',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'class_id': this.data.class_id,
        'class_name': e.detail.value.class_name,
        'class_teacher': e.detail.value.class_teacher,
        'class_size': e.detail.value.class_size,
        'class_intro': e.detail.value.class_intro,
        'class_creater': app.globalData.student_id //班级创建人信息
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res里面要有一个state和一个info，如果成功就在info里说成功，下面的弹窗会提醒。
        console.log(res)
        if (res.data.state == 1) {
          wx.showToast({   //弹窗提醒
            title: res.data.info
          });
        } else {
          wx.showToast({
            title: res.data.info
          });
        }
      }
    })
  },

  /**
   * 页面的初始数据
   */
  onLoad: function (options) {
    this.setData({ class_id: app.globalData.last_class_id+1 }) //页面加载时自动获取id
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
  
})