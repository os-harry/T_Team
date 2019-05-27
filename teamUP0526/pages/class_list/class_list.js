// pages/class_list/class_list.js
var app=getApp();

Page({
  /**
   * 页面的初始数据
   */
  data: {
    user: {name:'啊啊啊', id:'2016aaaaaa', fname:'啊'},
    class_data: [{ id: 1, name: "算法", teacher: "刘青", student_numbers: 56, team_numbers: 5 }, { id: 2, name: "软件工程", teacher: "刘青", student_numbers: 72,team_numbers: 9 }],
    actionSheetHidden: true
  },
  //页面的js动态效果
  actionSheetTap: function (options) {
    this.setData({
      actionSheetHidden: !this.data.actionSheetHidden
    })
  },
  bindjoin: function (e) {
    console.log('click', e)
    wx.navigateTo({
      url: '../class_join/class_join',
    })
  },
  bindcreate: function (e) {
    console.log('click', e)
    wx.navigateTo({
      url: 'pages/class_create/class_create',
    })
  },
  actionSheetChange: function (options) {
    this.setData({
      actionSheetHidden: !this.data.actionSheetHidden
    })
  },
  //选择进入某个班级的传参
  go_into_class: function(e){
    app.globalData.class_id=e.currentTarget.dataset.classid
    console.log('传入的班级id为：',e.currentTarget.dataset.classid)
    wx.navigateTo({  //页面跳转
      url: '../team_list/team_list',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {  //页面加载时向后台请求数据
    wx.request({
      url: 'http://127.0.0.1:5000/classList',//在这里加上后台的php地址
      data: { //发送给后台的数据
        //'student_id': app.globalData.student_id,
        'student_id': 1,
      },
      method: 'GET',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res.data里面要有state、info、student_info、classes（页面主要数据），如果成功就在info里说成功，下面的弹窗会提醒,不成功给出错误信息info。
        if (res.data.state == 1) { //用php返回的数据更新页面数据
          this.setData({user:res.data.student_info, class_data:res.data.classes}) 
        } else {
          console.log(res)
          wx.showToast({
            title: res.data.info
          });
        }
      }
    });
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