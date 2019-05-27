// pages/team_create/team_create.js
var app=getApp();
Page({
  /**
   * 页面的初始数据
   */
  data: {
    class_info: { id: 69321, name: "面向对象程序设计", sup: 5, teams_count: 5, single_list: ["张一一", "张二二", "张三三", "张五五", "张一一", "张二二", "张三三", "张五五", "张一一", "张二二"],last_team_id: 5},
    team: { id: 321, sup: 5, info: "在此可输入队伍名，队伍简介，队员要求等信息"},
    leader_name: "张一一",
    invitors:[]
  },

  // 获取多选框list中选中的值和对应的name

  checkboxChange: function (e) {
    console.log('选中的有：',e.detail.value);
    this.data.invitors=e.detail.value
  },

  formSubmit: function (e) {
    if(e.detail.value.leader_name==''){ //队长默认为创建人
      e.detail.value.leader_name=this.data.leader_name
    };
    console.log('form发生了submit事件，携带数据为：', e.detail.value,this.data.invitors)
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'leader_name': e.detail.value.leader_name,
        'team_info': e.detail.value.info,
        'team_invitors': this.data.invitors,
        'team_id': this.data.team.id,
        'team_sup': this.data.team.sup,
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res里面要有一个state和一个info，如果成功就在info里说成功，下面的弹窗会提醒。
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
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: ' ',//在这里加上后台的php地址
      data: { //发送给后台的数据
        'class_id': app.globalData.class_id,
        'student_id': app.globalData.student_id
      },
      method: 'POST',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      success: function (res) { //获取php的返回值res，res.data里面要有xxx，如果成功就在info里说成功，下面的弹窗会提醒,不成功给出错误信息info。
        if (res.data.state == 1) { //用php返回的数据更新页面数据      
          this.setData({ class_info: res.data.class_info, team: res.data.team, leader_name: res.data.leader_name}) //setData函数只能更新一整个类，无法单独更新数组和整个类的儿子
        } else {
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